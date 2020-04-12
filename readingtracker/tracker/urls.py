from django.urls import path

from . import views

app_name='tracker'

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.login_view, name='login'),
	path('addBook/', views.addBook, name='addBook')
]