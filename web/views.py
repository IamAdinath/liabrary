from django.shortcuts import render

# Create your views here.

def books(request):
    return render('books.html', context="Bla bla")