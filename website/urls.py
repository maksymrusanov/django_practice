from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.main, name='main'),
    path('top_rated', views.top_rated, name='top_rated'),
]
