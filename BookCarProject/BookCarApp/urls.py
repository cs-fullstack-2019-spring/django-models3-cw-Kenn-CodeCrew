from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('books/new/', views.new, name="new"),
    path('books/all/', views.all, name="all"),
    path('books/greaterThan18/', views.greater, name="all"),
    path('books/update/', views.update, name="all"),
]