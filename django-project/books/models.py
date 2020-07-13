from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Books(models.Model):
	title	= models.CharField(max_length=255)
	content = models.TextField()
	genre	= models.CharField(max_length=255)
	author  = models.CharField(max_length=255)
	published = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug	= models.SlugField(blank=True, editable=False)

	def save(self):
		self.slug =	slugify(self.title)
		super().save()


	def get_absolute_url(self):
		url_slug = {'slug':self.slug}
		return reverse('books:detail', kwargs=url_slug)

	def __str__(self):
		return "{}. {}".format(self.id, self.title)