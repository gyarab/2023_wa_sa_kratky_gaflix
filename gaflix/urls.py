
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from filmy.views import movies, movie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='filmy/prvni.html'), name='home'),
    path('druha/', TemplateView.as_view(template_name='filmy/druha.html'), name='druha'),
    path('movies/', movies, name="movies"),
    path('movie/<int:id>', movie, name="movie"),
]
