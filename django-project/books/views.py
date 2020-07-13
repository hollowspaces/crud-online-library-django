from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

#load model
from .models import Books
from .forms import BooksForm


# Create your views here.

class BooksPerGenre():
	model = Books

	def get_latest_books_each_genre(self):
		genre_list = self.model.objects.values_list('genre', flat=True).distinct()
		queryset = []
		
		# untuk setiapgenre di dalam genre_list
		# maka setiap objek dalam genre akan di retrieve datanya sesuai genre
		# kemudian data yang diambil data paling baru sesuai dengan published
		# setelah itu menambah ke queryset dengan append
		for genre in genre_list:
			books = self.model.objects.filter(genre=genre).latest('published')
			queryset.append(books)
		return queryset

class BooksUpdateView(UpdateView):
	form_class = BooksForm
	model = Books
	template_name = "books/content_update.html"

class BooksDeleteView(DeleteView):
	model = Books
	template_name = "books/delete_confirmation.html"
	success_url = reverse_lazy('books:manage')

class BooksManageView(ListView):
	model = Books
	template_name = "books/content_manage.html"
	context_object_name = 'books_list'

class BooksCreateView(CreateView):
	form_class = BooksForm
	template_name = 'books/content_create.html'


class GenreListView(ListView):
	model 		  = Books
	template_name ="books/books_genre_list.html"
	context_object_name = 'books_list'
	ordering 	  = ['-published']
	paginate_by	  = 4

	def get_queryset(self):
		self.queryset = self.model.objects.filter(genre=self.kwargs['genre'])
		return super().get_queryset()

	def get_context_data(self, *args, **kwargs):
		genre_list = self.model.objects.values_list('genre', flat=True).distinct().exclude(genre=self.kwargs['genre'])
		self.kwargs.update({'genre_list':genre_list})
		kwargs = self.kwargs
		return super().get_context_data(*args, **kwargs)


class ContentListView(ListView):
	model 		  = Books
	template_name = "books/content_list.html"
	context_object_name = 'books_list'
	ordering 	  = ['-published']
	paginate_by   = 4

	def get_context_data(self, *args, **kwargs):
		genre_list = self.model.objects.values_list('genre', flat=True).distinct()
		self.kwargs.update({'genre_list':genre_list})
		kwargs = self.kwargs
		return super().get_context_data(*args, **kwargs)


class ContentDetailView(DetailView):
	model 		  = Books
	template_name = "books/content_detail.html"
	context_object_name = 'books'