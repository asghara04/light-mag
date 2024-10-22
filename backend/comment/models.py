from django.db import models
from article.models import Article

class CPublished(models.Manager):
	def get_queryset(self):
		return super(CPublished, self).get_queryset().filter(status=True, personal=False)

class RPublished(models.Manager):
	def get_queryset(self):
		return super(RPublished, self).get_queryset().filter(status=True)

class UnRead(models.Manager):
	def get_queryset(self):
		return super(UnRead, self).get_queryset().filter(readed=False)

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name="comments")
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	date = models.DateTimeField(auto_now_add=True)
	message = models.TextField(max_length=350)
	personal = models.BooleanField(default=False)
	status = models.BooleanField(default=False)
	readed = models.BooleanField(default=False)

	objects = models.Manager()
	published = CPublished()
	unread = UnRead()

	def reps(self):
		return self.replies.filter(status=True).count()

	def __str__(self):
		return str(self.id)
	class Meta:
		ordering = ("-id",)


class Reply(models.Model):
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	date = models.DateTimeField(auto_now_add=True)
	message = models.TextField(max_length=250)
	status = models.BooleanField(default=False)
	readed = models.BooleanField(default=False)

	objects = models.Manager()
	published = RPublished()
	unread = UnRead()

	def __str__(self):
		return str(self.id)