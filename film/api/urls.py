from . import views
from django.urls import path
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Movies and Commments API')

urlpatterns = [
    path('', views.api_root),
    path('schema/', schema_view),
    path('movies/', views.MoviesList.as_view(), name='moviesList'),
]