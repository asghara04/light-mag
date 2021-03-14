from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Image
from .serializer import ImageSerializer
from rest_framework.permissions import IsAdminUser
from django.http import Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
from lightmag.pagination import PaginationMixin

nameUniqueError = {"name":["تصویر دیگری با همین نام وجود دارد."]}

def unqiue_names(name):
	for image in Image.objects.all():
		if name==image.name:
			return False
	return True
def unqiue_name(name,pk):
	for image in Image.objects.all():
		if name==image.name and pk!=image.id:
			return False
	return True

class ImagesView(APIView, PaginationMixin):
	permission_classes = (IsAdminUser,)
	pagination_class = PageNumberPagination()
	renderer_classes = (JSONRenderer,)
	def get(self, request):
		images = Image.objects.all()
		page = self.paginate_queryset(images)
		if page is not None:
			serializer = self.get_paginated_response(ImageSerializer(page, many=True, context={"request":request}).data)
		else:
			serializer = ImageSerializer(images, many=True, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	def post(self, request):
		serializer = ImageSerializer(data=request.data, context={"request":request})
		if serializer.is_valid():
			if unqiue_names(request.data['name']):
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(nameUniqueError, status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImagesCountView(APIView):
	permission_classes = (IsAdminUser,)
	renderer_classes = (JSONRenderer,)
	def get(self, request, fromat=None):
		imgs_count = Image.objects.all().count()
		content = {"count": imgs_count}
		return Response(content, status=status.HTTP_200_OK)


class ImageView(APIView):
	permission_classes = (IsAdminUser,)
	renderer_classes = (JSONRenderer,)
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
			if request.data['name'] and unqiue_name(request.data['name'],image.id):
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			return Response(nameUniqueError,status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, pk):
		image = self.get_img(pk)
		image.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)