from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


from .models import Book
from .forms import BookForm

# Create your views here.
def base(request):
    return HttpResponse('hello world')

# def books_list(request):
#     books = Book.objects.all()
#     return render (request, 'core/books_list.html', {"books": books})
 
def books_list(request):
    books = Book.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'core/books_list.html', {})