from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


from .models import Book, Category
from .forms import BookForm

# Create your views here.
def base(request):
    return HttpResponse('hello world')

def books_list(request):
    books = Book.objects.order_by('-created_at')
    return render(request, 'core/books_new.html', {"books": books})
    

def books_old(request):
    books = Book.objects.order_by('created_at')
    return render(request, 'core/books_old.html', {"books": books})

def books_title(request):
    books = Book.objects.order_by('title')
    return render(request, 'core/books_title.html', {"books": books})

def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books_for_category=Book.objects.filter(category=category)
    return render(request, 'core/books_by_category.html', {'books':books_for_category, 'category': category })