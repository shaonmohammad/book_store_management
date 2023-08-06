from django import forms
from . import models


class BookStoreForm(forms.ModelForm):
    class Meta:
        model = models.BookModels
        exclude = ['first_pub', 'last_pub']
