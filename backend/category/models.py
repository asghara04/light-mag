from django.db import models
from image.models import Image

class Category(models.Model):
	image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=25, unique=True)
	slug = models.SlugField(max_length=25, unique=True)

	def __str__(self):
		return self.name
	class Meta:
		ordering = ("-id",)


class SubCat(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcats")
	image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=25)
	slug = models.SlugField(max_length=25, unique=True)

	unique_together = ("categpry", "name")

	def __str__(self):
		return self.name
	class Meta:
		ordering = ("-id",)