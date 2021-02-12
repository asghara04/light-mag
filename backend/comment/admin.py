from django.contrib import admin
from .models import Comment, Reply

admin.site.register(Comment)
admin.site.register(Reply)