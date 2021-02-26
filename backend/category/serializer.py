from rest_framework import serializers
from .models import Category, SubCat
from image.serializer import ImageSerializer
from django.shortcuts import get_object_or_404


class SubCatSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	category = serializers.StringRelatedField()
	image = ImageSerializer()
	name = serializers.CharField(max_length=25)
	slug = serializers.SlugField(max_length=25)

	def validate_image(self, value):
		return get_object_or_404(Image, name=value["name"])

	def create(self, validated_data):
		return SubCat.Object.Create(**validated_data)
	def update(self, instance, validated_data):
		instance.category = validated_data.get("category", instance.category)
		instance.image = validated_data.get("image", instance.image)
		instance.name = validated_data.get("name", instance.name)
		instance.slug = validated_data.get("slug", instance.slug)
		instance.save()
		return instance


class CategorySerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	image = ImageSerializer()
	name = serializers.CharField(max_length=25)
	slug = serializers.SlugField(max_length=25)
	subcats = SubCatSerializer(many=True)

	def validate_image(self, value):
		return get_object_or_404(Image, name=value["name"])

	def create(self, validated_data):
		return Category.objects.create(**validated_data)
	def post(self, instance, validated_data):
		instance.image = validated_data.get("image", instance.image)
		instance.name = validated_data.get("name", instance.name)
		instance.slug = validated_data.get("slug", instane.slug)
		instance.save()
		return instance