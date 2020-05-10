from django.urls import path

from . import views

app_name='tracker'

urlpatterns = [
	path('', views.index, name='index'),
	path('addBook/', views.addBook, name='addBook'),
	path('deleteBook/<int:pk>/', views.deleteBook, name='deleteBook'),
	path('moveBook/<int:pk>/', views.moveBook, name='moveBook'),
	path('profile/', views.displayProfile, name='displayProfile'),
	path('deleteAccount/', views.deleteAccount, name='deleteAccount'),
	path('books/', views.showBooks, name='showBooks')

]