from rest_framework import serializers
from .models import User
from image.serializer import ImageSerializer
from category.serializer import CategorySerializer
from django.shortcuts import get_object_or_404
from image.models import Image
from category.models import Category

class UserSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	username = serializers.SlugField(max_length=30)
	name = serializers.CharField(max_length=35 )
	prof_picture = ImageSerializer()
	pubmail = serializers.EmailField(max_length=30)
	bio = serializers.CharField(max_length=400)
	about = serializers.CharField(max_length=400)
	favorite_cat = CategorySerializer()
	instagram_link = serializers.URLField(max_length=35)
	facebook_link = serializers.URLField(max_length=35)
	github_link = serializers.URLField(max_length=35)
	jbirth = serializers.DateField(read_only=True)
	pubartcount = serializers.IntegerField(read_only=True)


class MUserSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	email = serializers.EmailField(max_length=30)
	password = serializers.CharField()
	username = serializers.SlugField(max_length=30)
	prof_picture = ImageSerializer()
	name = serializers.CharField(max_length=35)
	jjoin = serializers.DateField(read_only=True)
	jlast = serializers.DateField(read_only=True)
	is_active = serializers.BooleanField(default=True)
	is_staff = serializers.BooleanField(default=False)
	pubmail = serializers.EmailField(max_length=30,allow_null=True)
	bio = serializers.CharField(max_length=400, allow_null=True)
	about = serializers.CharField(max_length=400, allow_null=True)
	favorite_cat = CategorySerializer(allow_null=True)
	instagram_link = serializers.URLField(max_length=35, allow_null=True)
	facebook_link = serializers.URLField(max_length=35, allow_null=True)
	github_link = serializers.URLField(max_length=35, allow_null=True)
	jbirth = serializers.DateField(allow_null=True,read_only=True)
	birthday = serializers.DateField(allow_null=True)
	artcount = serializers.IntegerField(read_only=True)

	def validate_prof_picture(self, value):
		return get_object_or_404(Image,  name=value["name"])
	def validate_favorite_cat(self, value):
		return get_object_or_404(Category, name=value["name"])
	def create(self, validated_data):
		user = User.objects.create(**validated_data)
		user.set_password(validated_data["password"])
		user.save()
		return user
	def update(self, instance, validated_data):
		instance.email = validated_data.get("email", instance.email)
		instance.password = validated_data.get("password", instance.password)
		instance.username = validated_data.get("username", instance.username)
		instance.name = validated_data.get("name", instance.name)
		instance.prof_picture = validated_data.get("prof_picture", instance.prof_picture)
		instance.is_active = validated_data.get("is_active", instance.is_active)
		instance.is_staff = validated_data.get("is_staff", instance.is_staff)
		instance.pubmail = validated_data.get("pubmail", instance.pubmail)
		instance.bio = validated_data.get("bio", instance.bio)
		instance.about = validated_data.get("about", instance.about)
		instance.favorite_cat = validated_data.get("favorite_cat", instance.favorite_cat)
		instance.instagram_link = validated_data.get("instagram_link", instance.instagram_link)
		instance.facebook_link = validated_data.get("facebook_link", instance.facebook_link)
		instance.github_link = validated_data.get("github_link", instance.github_link)
		instance.birthday = validated_data.get("birthday", instance.birthday)
		instance.save()
		return instance


class MinUserSerializer(serializers.Serializer):
	username = serializers.SlugField(max_length=30)
	name = serializers.CharField(max_length=35)
	prof_picture = ImageSerializer(read_only=True)