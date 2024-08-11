from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.db.models import Avg , Max, Min


from .models import Book

# Create your views here.

def index(request):
    books= Book.objects.all().order_by('-rating')
    book_count = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request,"book_store/index.html",{
        'data': books,
        'book_count' :book_count,
        'avg_rating': avg_rating.get('rating__avg'),

    })

def book(request,slug):
    #Note: Long Way
    # try:
    #     book= Book.objects.get(pk=book_id)
    #     print(book)
    # except ObjectDoesNotExist:
    #     raise Http404()
    
    #Note: Short cut - by ID (param need to be book_id)
    # book = get_object_or_404(Book,pk=book_id)

    #Note: Short cut - by slug
    book = get_object_or_404(Book,slug=slug)
    
    return render(request,"book_store/book_detail.html",{
        'book': book,
        'data': book,
    })
