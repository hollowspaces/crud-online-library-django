from django.views.generic import TemplateView
from books.views import BooksPerGenre

class WebHomeView(TemplateView, BooksPerGenre):
	template_name = 'index.html'

	def get_context_data(self):
		queryset= self.get_latest_books_each_genre()
		context = {
			'latest_book_list':queryset,
		}

		return context