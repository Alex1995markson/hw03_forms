from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post, Group, User


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def profile(request, username):
    if (username):
        user_info = get_object_or_404(User, username=username)
        posts_profile = user_info.post_set.all()
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
    post = get_object_or_404(Post, pk=post_id)
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
        form = PostForm(request.POST)
        if form.is_valid():
            data_form = form.save(commit=False)
            data_form.author = username = request.user
            data_form.save()
            return redirect('main:profile', username)
        else:
            print(form.errors)
    else:
        form = PostForm()
    return render(request, 'posts/post_create.html',
                  {'form': form,
                   'card': 'Создание поста',
                   'title': 'Страница создания поста',
                   'head': 'Создай новый пост'})


@login_required
def post_edit(request, post_id):
    post_change = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=post_change)
    if form.is_valid():
        post_change = form.save(commit=True)
        return redirect('main:post_detail', post_id)
    else:
        context = {'form': form,
                   'card': 'Редактирование поста',
                   'title': 'Страница редактирования поста',
                   'head': 'Редактируй пост'}
        return render(request, 'posts/post_create.html', context)
