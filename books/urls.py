"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.books_list, name='books_list'),
    path('books/<slug:slug>/', views.books_by_category, name='books-by-category'), 
    path('books/old', views.books_old, name='books_old'),
    path('books/title', views.books_title, name='books_title'),
    # path('accounts/', include('registration.backends.default.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

