from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import *
# Create your views here.

class Index(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'index.html'


class BookReadView(BSModalReadView):
    model = Book
    template_name = 'read_book1.html'

class BookCreateView(BSModalCreateView):
    template_name = 'create_book.html'
    form_class = BookModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('index')