from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView


from .views import WebHomeView

urlpatterns = [
	re_path('^$', WebHomeView.as_view(template_name='index.html'), name='home'),
	path('books/', include('books.urls', namespace='books'), name='list'),
	path('admin/', admin.site.urls),
	
    
]
