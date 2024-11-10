from django.utils import timezone
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import redirect
from .forms import PostForm

from django.views.generic import ListView, DetailView
from .models import Post

def post_list(request):
    posts = Post.objects.published()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.published()

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'



def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():  # Проверяем валидность формы
            post = form.save(commit=False)
            post.author = request.user  # Привязываем автора (предполагаем, что пользователь авторизован)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')  # Перенаправляем на список постов после сохранения
        else:
            # Если форма не валидна, отобразим ошибки на странице
            return render(request, 'blog/post_form.html', {'form': form})
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})