from django.shortcuts import render
from django.http import HttpResponse

from .models import Book
from .forms import BookForm

# Create your views here.
def base(request):
    return HttpResponse('hello world')

def books_list(request):
    books = Book.objects.all()
    return render (request, 'core/books_list.html', {"books": books})
