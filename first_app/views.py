from django.shortcuts import render, redirect

from . forms import BookStoreForm
from . models import BookModels
# Create your views here.


def home(request):
    return render(request, "./base.html")


def store_book(request):

    if request.method == 'POST':
        forms = BookStoreForm(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
            forms.save()
            return redirect('show_books')

    else:
        forms = BookStoreForm()

    return render(request, "./store_book.html", {'forms': forms})


def show_book(request):
    book = BookModels.objects.all()
    return render(request, "./show_book.html", {'books': book})


def edit_book(request, id):
    book = BookModels.objects.get(pk=id)
    form = BookStoreForm(instance=book)
    if request.method == "POST":
        form = BookStoreForm(request.POST, instance=book)
        if form.is_valid:
            form.save()
            return redirect('show_books')
    return render(request, "./store_book.html", {'forms': form})


def delete_book(request, id):
    book = BookModels.objects.get(pk=id).delete()
    return redirect('show_books')
