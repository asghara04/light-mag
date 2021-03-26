from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(max_length=25)
	slug = serializers.CharField(max_length=25)
	
	def create(self, validated_data):
		return Tag.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.name = validated_data.get("name", instance.name)
		instance.slug = validated_data.get("slug", instance.slug)
		instance.save()
		return instance