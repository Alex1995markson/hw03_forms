from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post, Group, User
from .forms import PostForm


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def profile(request, username):
    if (username):
        user_info = User.objects.get(username=username)
        posts_profile = Post.objects.filter(author=user_info.id)
        paginator = Paginator(posts_profile, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'author': user_info
        }
        return render(request, 'posts/profile.html', context)
    else:
        return render(request, '404.html', status=404)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'posts/post_detail.html', {"post": post})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts_groups = group.posts.all()
    paginator = Paginator(posts_groups, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'group': group

    }
    return render(request, "posts/group_list.html", context)


@login_required
def post_create(request):

    if request.method == 'POST':
        form = PostForm(request.POST)  # autor=username
        print('Here')
        if form.is_valid():  # is the form valid?
            value_form = form.save(commit=False)  # yes? save to database
            value_form.author = username = request.user
            value_form.save()
            print('after save')
            return redirect('main:profile', username)
        else:
            print(form.errors)  # no? display errors to end user
    else:
        form = PostForm()
    return render(request, 'posts/post_create.html', {'form': form})


@login_required
def post_edit(request, post_id):
    obj= get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance= obj)
    context= {'form': form}
    if form.is_valid():
        obj= form.save(commit= False)

        obj.save()

        # messages.success(request, "You successfully updated the post")

        context= {'form': form}
        return redirect('main:post_detail', post_id)
        # return render(request, 'posts/pos.html', context)

    else:
        context= {'form': form,
                           'error': 'The form was not updated successfully. Please enter in a title and content'}
        return render(request,'posts/post_create.html' , context)
    # print(obj)
    # print(form)
    # if request.method == 'POST':
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=True)
    #         author = Post.author.objects.get(pk=post_id)
    #         print(author)
    # else:
    #     form = PostForm()
    return render(request, 'posts/post_create.html', context)
