from django.contrib import admin
from django.urls import path
from amazon.books.views import authors_list
from amazon.books.views import authors_detail


urlpatterns = [
    path('admin/', admin.site.urls),

    path('authors/', authors_list,
            name='authors-list'),
    path('authors/<int:pk>/', authors_detail,
            name='authors-detail'),
]
