from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST


from .models import Book
from .forms import BookForm


# Create your views here.
def index(request):
	book_list = Book.objects.all()
	form = BookForm()
	context = {
		'book_list' : book_list,
		'form' : form
	}
	return render(request, 'tracker/index.html', context)

@require_POST
def addBook(request):
	newBookForm = BookForm(request.POST)
	if newBookForm.is_valid():
		new_book = newBookForm.save()
	return redirect('tracker:index')

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			return redirect('tracker:index')
	else:
		form = AuthenticationForm()
	return render(request, 'tracker/login.html', {'form': form})

