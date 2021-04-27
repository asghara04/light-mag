from django.db import models
from django.utils import timezone
from image.models import Image
from category.models import Category, SubCat
from user.models import User
from tag.models import Tag

class Published(models.Manager):
	def get_queryset(self):
		return super(Published, self).get_queryset().filter(status="public")


class Article(models.Model):
	STATUSES = (("public", "public"), ("draft", "draft"))
	title = models.CharField(max_length=120,unique=True)
	slug = models.SlugField(max_length=120, unique=True)
	image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
	description = models.TextField(max_length=200)
	body = models.TextField(max_length=999999)
	date = models.DateTimeField(auto_now_add=True)
	publish_date = models.DateTimeField(default=timezone.now)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	subcat = models.ForeignKey(SubCat, on_delete=models.SET_NULL, null=True, blank=True)
	tags = models.ManyToManyField(Tag, blank=True)
	status = models.CharField(max_length=8, choices=STATUSES)
	author = models.ForeignKey(User, on_delete=models.SET_DEFAULT,related_name='arts',default="asghar")

	read_time_m = models.IntegerField(default=3)

	objects = models.Manager()
	published = Published()

	def coms(self):
		return self.comments.filter(status=True).count()

	def __str__(self):
		return self.slug
	class Meta:
		ordering = ("-id",)