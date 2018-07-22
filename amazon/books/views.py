from django.shortcuts import render
from amazon.books.models import Author, Book
from django.views.generic import ListView
from django.views.generic import DetailView


class AuthorList(ListView):
    model = Author
    template_name = 'authors.html'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author_detail.html'


authors_list = AuthorList.as_view()
authors_detail = AuthorDetail.as_view()

# def authors_list(request):
#     authors = Author.objects.all()
#     return render(request, 'authors.html', {
#         'authors': authors
#     })
