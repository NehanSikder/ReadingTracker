from django import forms
from .models import Book

class BookForm(forms.ModelForm):

	name = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class': "form-control mr-1"}))


	class Meta:
		model = Book
		exclude = ['user']
