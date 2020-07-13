from django.urls import re_path

from .views import (
	ContentListView, 
	ContentDetailView, 
	GenreListView, 
	BooksCreateView, 
	BooksManageView, 
	BooksDeleteView, 
	BooksUpdateView,
)

app_name = 'list'
app_name = 'detail'
app_name = 'add'

urlpatterns = [
	re_path('^manage/update/(?P<pk>\d+)$', BooksUpdateView.as_view(), name='update'),
	re_path('^manage/delete/(?P<pk>\d+)$', BooksDeleteView.as_view(), name='delete'),
	re_path('^manage/$', BooksManageView.as_view(), name='manage'),
	re_path('^add/$', BooksCreateView.as_view(), name='add'),
	re_path('^genre/(?P<genre>[\w-]+)/(?P<page>\d+)$', GenreListView.as_view(), name='genres'),
	re_path('^detail/(?P<slug>[\w-]+)$', ContentDetailView.as_view(), name='detail'),
	re_path('^(?P<page>\d+)$', ContentListView.as_view(), name='list'),    
]
