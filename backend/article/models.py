from django.db import models
from image.models import Image
from category.models import Category, SubCat
from user.models import User
from tag.models import Tag
import jdatetime

def set_jdatetime(gdate):
	jdatetime.set_locale("fa_IR")
	return jdatetime.datetime.fromgregorian(year=gdate.year,month=gdate.month,day=gdate.day,hour=gdate.hour,minute=gdate.minute,second=gdate.second).strftime("%d %B %Y, %H:%M")

class Published(models.Manager):
	def get_queryset(self):
		return super(Published, self).get_queryset().filter(status="عمومی")


class Article(models.Model):
	STATUSES = (("عمومی", "عمومی"), ("پیشنویس", "پیشنویس"))
	title = models.CharField(max_length=80)
	slug = models.SlugField(max_length=80, unique=True)
	image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
	description = models.TextField(max_length=200)
	body = models.TextField(max_length=2048)
	date = models.DateTimeField(auto_now_add=True)
	publish_date = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	subcat = models.ForeignKey(SubCat, on_delete=models.SET_NULL, null=True, blank=True)
	tags = models.ManyToManyField(Tag, blank=True)
	status = models.CharField(max_length=8, choices=STATUSES)
	author = models.ForeignKey(User, on_delete=models.SET_DEFAULT,related_name='author',default="asghar")

	objects = models.Manager()
	published = Published()

	def jpub_date(self):
		return set_jdatetime(self.publish_date)
	def jdate(self):
		return set_jdatetime(self.date)

	def coms(self):
		return self.comments.filter(status=True).count()
	
	def __str__(self):
		return self.slug
	class Meta:
		ordering = ("-id",)