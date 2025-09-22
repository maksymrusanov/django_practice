from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.popular_film, name='popular_film'),
    path('top_rated', views.top_rated, name='top_rated'),
]
