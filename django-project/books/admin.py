from django.contrib import admin

# Register your models here.
from .models import Books

class BooksUpdate(admin.ModelAdmin):
	readonly_fields=[
		'slug',
		'updated',
		'published',
	]

admin.site.register(Books, BooksUpdate)