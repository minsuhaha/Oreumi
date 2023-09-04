from django.shortcuts import render
from haystack.query import SearchQuerySet

def search_view(request):
    query = request.GET.get('q')
    
    if query:
        books = SearchQuerySet().filter(content=query)
    else:
        books = []

    return render(request, 'books/search_results.html', {'books': books})
