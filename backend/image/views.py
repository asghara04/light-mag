from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Image
from .serializer import ImageSerializer
from rest_framework.permissions import IsAdminUser
from django.http import Http404


class ImagesView(APIView):
	permission_classes = (IsAdminUser,)
	def get(self, request):
		images = Image.objects.all()
		serializer = ImageSerializer(images, many=True, context={"request":request})
		return Response(serializers.data, status=status.HTTP_200_OK)
	def post(self, request):
		serialazer = ImageSerializer(data=request.data, context={"request":request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageView(APIView):
	permission_classes = (IsAdminUser,)
	def get_img(self, pk):
		try:
			return Image.objects.get(id=pk)
		except:
			raise Http404
	def get(self, request, pk):
		image = self.get_img(pk)
		serializer = ImageSerializer(image, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	def patch(self, request, pk):
		image = self.get_img(pk)
		serializer = ImageSerializer(image, request.data, partial=True, context={"request":request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, pk):
		image = self.get_img(pk)
		image.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)