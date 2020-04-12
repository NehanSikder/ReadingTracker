from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


from .models import Book
from .forms import BookForm


# Create your views here.
@login_required
def index(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.get_username()
	book_list = Book.objects.all()
	form = BookForm()
	context = {
		'book_list' : book_list,
		'form' : form,
		'username' : username,
	}
	return render(request, 'tracker/index.html', context)

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

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			return redirect('tracker:index')
	else:
		form = AuthenticationForm()
	return render(request, 'registration/login.html', {'form': form})

