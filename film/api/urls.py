from . import views
from django.urls import path
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Movies and Commments API')

urlpatterns = [
    path('', views.api_root),
    path('schema/', schema_view),
    path('movies/', views.MoviesList.as_view(), name='moviesList'),
    path('movies/<int:pk>/', views.MoviesItem.as_view(), name='moviesItem'),
    path('comments/', views.CommentsList.as_view(), name='commentsList'),
    path('comments/<int:pk>/', views.CommentsItem.as_view(), name='commentsItem'),
]