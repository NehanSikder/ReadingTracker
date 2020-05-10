from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Book
from .forms import BookForm

from datetime import datetime
import json

# Create your views here.
@login_required
def index(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.get_username()
	book_list = Book.objects.all().filter(user=username).order_by('-completed_date_time')
	# interate through book_list and create subset
	book_list_completed = []
	book_list_remaining = []
	books_completed_per_month = {}
	for book in book_list:
		if book.already_read:
			if book.completed_date_time:
				date_str = book.completed_date_time.strftime("%Y-%m-%d")
				count = books_completed_per_month.get(date_str)
				if count:
					count = count+1
					books_completed_per_month[date_str] = count
				else:
					books_completed_per_month[date_str] = 1
			book_list_completed.append(book)
		else:
			book_list_remaining.append(book)
	form = BookForm()
	context = {
		'book_list_completed' : book_list_completed,
		'book_list_remaining' : book_list_remaining, 
		'book_list_completed_number' : len(book_list_completed),
		'book_list_remaining_number' : len(book_list_remaining), 
		'book_completed_months': json.dumps(list(books_completed_per_month.keys())),
		'book_completed_count': json.dumps(list(books_completed_per_month.values())),
		'form' : form,
		'username' : username,
	}
	return render(request, 'tracker/index.html', context)

@login_required
def showBooks(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.get_username()
	book_list = Book.objects.all().filter(user=username).order_by('-completed_date_time')
	# interate through book_list and create subset
	book_list_completed = []
	book_list_remaining = []
	books_completed_per_month = {}
	for book in book_list:
		if book.already_read:
			if book.completed_date_time:
				date_str = book.completed_date_time.strftime("%Y-%m-%d")
				count = books_completed_per_month.get(date_str)
				if count:
					count = count+1
					books_completed_per_month[date_str] = count
				else:
					books_completed_per_month[date_str] = 1
			book_list_completed.append(book)
		else:
			book_list_remaining.append(book)
	form = BookForm()
	context = {
		'book_list_completed' : book_list_completed,
		'book_list_remaining' : book_list_remaining, 
		'book_list_completed_number' : len(book_list_completed),
		'book_list_remaining_number' : len(book_list_remaining), 
		'book_completed_months': json.dumps(list(books_completed_per_month.keys())),
		'book_completed_count': json.dumps(list(books_completed_per_month.values())),
		'form' : form,
		'username' : username,
	}
	return render(request, 'tracker/books.html', context)

@login_required
def deleteAccount(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.get_username()
	Book.objects.all().filter(user=username).delete()
	User.objects.get(username=username).delete()
	# log out user
	logout(request)
	return redirect('/accounts/login/')


@login_required
def displayProfile(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.get_username()
	# Get profile object using username
	profile = User.objects.get(username=username)
	context = {
		'profile' : profile,
	}
	return render(request, 'tracker/profile.html', context)

@require_POST
def addBook(request):
	newBookForm = BookForm(request.POST)
	if newBookForm.is_valid():
		new_book = newBookForm.save(commit=False)
		new_book.user = request.user.get_username()
		newBookForm.save()
	return redirect('tracker:index')

def deleteBook(request,pk):
	Book.objects.filter(id=pk).delete()
	return redirect('tracker:index')

def moveBook(request,pk):
	book = Book.objects.get(pk=pk)
	book.already_read = not book.already_read
	if book.already_read:
		book.completed_date_time = datetime.now()
	else:
		book.completed_date_time = None
	book.save()
	return redirect('tracker:index')

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			return redirect('tracker:index')
	else:
		form = AuthenticationForm()
	return render(request, 'registration/login.html', {'form': form})

def signUp(request):
	if request.method == 'POST':
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('tracker:index')
	else:
		form = UserCreationForm()
	return render(request, 'registration/signUp.html', {'form': form})

	

