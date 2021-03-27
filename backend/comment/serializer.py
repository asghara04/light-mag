from rest_framework import serializers
from .models import Comment, Reply
from article.models import Article


class CommentSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	article = serializers.PrimaryKeyRelatedField(queryset=Article.published.all())
	name = serializers.CharField(max_length=30)
	email = serializers.EmailField(max_length=30,write_only=True)
	jdate = serializers.DateTimeField(read_only=True)
	message = serializers.CharField(max_length=350)
	reps = serializers.IntegerField(read_only=True)

	def create(self, validated_data):
		return Comment.objects.create(**validated_data)

class ReplySerializer(serializers.Serializer):
	comment = serializers.PrimaryKeyRelatedField(queryset=Comment.published.all())
	name = serializers.CharField(max_length=30)
	email = serializers.EmailField(max_length=30,write_only=True)
	jdate = serializers.DateTimeField(read_only=True)
	message = serializers.CharField(max_length=250)

	def create(self, validated_data):
		return Reply.objects.create(**validated_data)



class MReplySerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all())
	name = serializers.CharField(max_length=30)
	email = serializers.EmailField(max_length=30)
	jdate = serializers.DateTimeField(read_only=True)
	message = serializers.CharField(max_length=250)
	status = serializers.BooleanField(default=False)
	readed = serializers.BooleanField(default=False)

	def create(self, validated_data):
		return Reply.objects.create(*validated_data)
	def update(self, instance, validated_data):
		instance.comment = validated_data.get("comment", instance.comment)
		instance.name = validated_data.get("name", instance.name)
		instance.email = validated_data.get("email", instance.email)
		instance.message = validated_data.get("message", instance.message)
		instance.status = validated_data.get("status", instance.status)
		instance.readed = validated_data.get("readed", instance.readed)
		instance.save()
		return instance


class MCommentSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all())
	name = serializers.CharField(max_length=30)
	email = serializers.EmailField(max_length=30)
	jdate = serializers.DateTimeField(read_only=True)
	message = serializers.CharField(max_length=350)
	personal = serializers.BooleanField(default=False)
	status = serializers.BooleanField(default=False)
	readed = serializers.BooleanField(default=False)
	reps = serializers.IntegerField(read_only=True)
	replies = MReplySerializer(read_only=True,many=True)

	def create(self, validated_data):
		return Comment.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.article = validated_data.get("article", instance.article)
		instance.name = validated_data.get("name", instance.name)
		instance.email = validated_data.get("email", instance.email)
		instance.message = validated_data.get("message", instance.message)
		instance.personal = validated_data.get("personal", instance.personal)
		instance.status = validated_data.get("status", instance.status)
		instance.readed = validated_data.get("readed", instance.readed)
		instance.save()
		return instance