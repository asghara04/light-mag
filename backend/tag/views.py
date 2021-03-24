from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tag
from .serializer import TagSerializer
from django.http import Http404
from rest_framework.permissions import IsAdminUser
from lightmag.pagination import PaginationMixin
from rest_framework.pagination import PageNumberPagination

class TagsView(APIView,PaginationMixin):
	permission_classes = (IsAdminUser,)
	pagination_class = PageNumberPagination()
	def get(self, request):
		tags = Tag.objects.all()
		page = self.paginate_queryset(tags)
		if page is not None:
			serializer = self.get_paginated_response(TagSerializer(page,many=True))
		else:
			serializer = TagSerializer(tags, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	def post(self, request):
		serializer = TagSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagView(APIView):
	def get_tag(self, pk):
		try:
			return Tag.objects.get(id=pk)
		except:
			raise Http404
	
	def get(self, request, pk):
		tag = self.get_tag(pk)
		serializer = TagSerializer(tag)
		return Response(serializers.data, status=status.HTTP_200_OK)
	def put(self, request, pk):
		tag = self.get_tag(pk)
		serializer = TagSerializer(tag, request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, pk):
		tag = self.get_tag(pk)
		tag.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)