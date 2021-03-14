from rest_framework import serializers
from .models import Article
from image.serializer import ImageSerializer
from category.serializer import CategorySerializer, SubCatSerializer
from user.serializer import MinUserSerializer
from django.shortcuts import get_object_or_404
from image.models import Image
from category.models import Category, SubCat
from tag.serializer import TagSerializer

class ArticleSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(read_only=True, max_length=80)
	slug = serializers.CharField(read_only=True, max_length=80)
	image = ImageSerializer(read_only=True)
	description = serializers.CharField(read_only=True, max_length=200)
	body = serializers.CharField(read_only=True, max_length=2048)
	jpub_date = serializers.DateTimeField(read_only=True)
	category = CategorySerializer(read_only=True)
	subcat = SubCatSerializer(read_only=True)
	tags = TagSerializer(many=True, read_only=True)
	author = MinUserSerializer(read_only=True)


class MArticleSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(max_length=80)
	slug = serializers.SlugField(max_length=80)
	image = ImageSerializer(allow_null=True)
	description = serializers.CharField(max_length=200)
	body = serializers.CharField(max_length=2048)
	jdate = serializers.DateTimeField(read_only=True)
	jpub_date = serializers.DateTimeField(read_only=True)
	category = CategorySerializer(allow_null=True)
	subcat = SubCatSerializer(allow_null=True)
	tags = TagSerializer(many=True, read_only=True)
	status = serializers.CharField(max_length=8)
	author = MinUserSerializer()
	
	def validate_image(self, value):
		return get_object_or_404(Image, name=value["name"])
	def validate_category(self, value):
		return get_object_or_404(Category, name=value["name"])
	def validate_SubCat(self, value):
		return get_object_or_404(SubCat, name=value["name"])
	def validate_author(self, value):
		return get_object_or_404(User, username=value["username"])
	def create(self, validated_data):
		return Article.objects.create(**validated_data)
	def update(self, inatance, validated_data):
		instance.title = validated_data.get("title", instance.title)
		instance.slug = validated_data.get("slug", instance.slug)
		instance.image = validated_data.get("image", instance.image)
		instance.description = validated_data.get("description", instance.description)
		instance.body = validated_data.get("body", instance.body)
		instance.category = validated_data.get("category", instance.category)
		instance.subcat = validated_data.get("subcat", instance.subcat)
		instance.status = validated_data.get("status", instance.status)
		instance.author = validated_data.get("author", instance.author)
		instance.save()
		return instance


class MinArticleSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(read_only=True, max_length=80)
	slug = serializers.SlugField(read_only=True, max_length=80)
	image = ImageSerializer(read_only=True)
	description = serializers.CharField(read_only=True, max_length=200)
	jpub_date = serializers.DateTimeField(read_only=True)
	# status = serializers.CharField(read_only=True, max_length=8)
	author = MinUserSerializer(read_only=True)