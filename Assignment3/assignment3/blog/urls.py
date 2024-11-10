from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),           # Отображение списка постов (CBV)
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Отображение одного поста (CBV)
    path('post/new/', views.add_post, name='post_create'),     # Создание нового поста
]
