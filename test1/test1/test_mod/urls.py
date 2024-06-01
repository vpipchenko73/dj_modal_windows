from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('read/<int:pk>', views.BookReadView.as_view(), name='read_book'),
    path('create/', views.BookCreateView.as_view(), name='create_book'),
]