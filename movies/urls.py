from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comments, name='comment'),
    path('movies/<int:movie_pk>/comments/<int:comment_pk>/', views.delete_comment, name='delete_comment'),
    path('movies/<int:pk>/likes/', views.likes, name='likes')
]
