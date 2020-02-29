from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


from .models import Book, Category
from .forms import BookForm

# Create your views here.
def base(request):
    return HttpResponse('hello world')

def books_list(request):
    books = Book.objects.all()
    return render (request, 'core/books_list.html', {"books": books})
 
# def books_list(request):
#     books = Book.objects.filter(created_at__lte=timezone.now()).order_by('created_date')
#     return render(request, 'core/books_list.html', {})

def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books_for_category=Book.objects.filter(category=category)
    return render(request, 'core/books_by_category.html', {'books':books_for_category, 'category': category })