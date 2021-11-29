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
    author_info = get_object_or_404(User, username=username)
    posts_profile = Post.objects.\
        prefetch_related('author').filter(author=author_info.id)
    paginator = Paginator(posts_profile, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'author': author_info
    }
    return render(request, 'posts/profile.html', context)


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
    form = PostForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'posts/post_create.html',
                      {'form': form,
                       'template_name': 'create'
                       })
    post_data = form.save(commit=False)
    post_data.author = request.user
    post_data.save()
    return redirect('main:profile', post_data.author)


@login_required
def post_edit(request, post_id):
    post_data = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=post_data)
    if (request.user is post_data.author):
        return redirect('main:post_detail', post_id)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('main:post_detail', post_id)
    context = {'form': form,
               'is_edit': True}
    return render(request, 'posts/post_create.html', context)
