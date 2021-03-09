from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	image = serializers.ImageField()
	alt = serializers.CharField(max_length=25)
	name = serializers.CharField(max_length=25)

	def create(self, validated_data):
		return Image.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.image = validated_data.get("image", instance.image)
		instance.alt = validated_data.get("alt", instance.alt)
		instance.name = validated_data.get("name", instance.name)
		instance.save()
		return instance