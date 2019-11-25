
from .models import Book
from django.contrib.auth.models import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm
from django import forms
from django.contrib.auth.models import User


class BookForm(BSModalForm):
    publication_date = forms.DateField(
        error_messages={'invalid': 'Enter a valid date in YYYY-MM-DD format.'}
    )

    class Meta:
        model = Book
        exclude = ['timestamp']

class CustomUserCreationForm(PopRequestMixin,CreateUpdateAjaxMixin, UserCreationForm):
	class Meta:
		model =User
		field = ['username'. 'password',' password2']