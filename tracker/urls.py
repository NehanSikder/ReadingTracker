from django.urls import path

from . import views

app_name='tracker'

urlpatterns = [
	path('', views.index, name='index'),
	path('addBook/', views.addBook, name='addBook'),
	path('deleteBook/<int:pk>/', views.deleteBook, name='deleteBook'),
]