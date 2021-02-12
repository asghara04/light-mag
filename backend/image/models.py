from django.db import models

class Image(models.Model):
	image = models.ImageField(upload_to="%Y/%m/%d")
	alt = models.CharField(max_length=25)
	name = models.CharField(max_length=25, unique=True)
	
	def __str__(self):
		return self.name
	class Meta:
		ordering = ("-id",)