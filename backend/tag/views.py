from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tag
from .serializer import TagSerializer
from django.http import Http404
from rest_framework.permissions import IsAdminUser
from lightmag.pagination import PaginationMixin
from rest_framework.pagination import PageNumberPagination


errs = {'name':[],'slug':[]}


def uniqueName(name,pk=False):
	for tag in Tag.objects.all():
		if (not pk and tag.name==name) or (pk and tag.id!=pk and tag.name==name):
			return False
	return True
def uniqueSlug(slug,pk=False):
	for tag in Tag.objects.all():
		if (not pk and tag.slug==slug) or (pk and tag.id!=pk and tag.slug==slug):
			return False
	return True


class TagsView(APIView,PaginationMixin):
	permission_classes = (IsAdminUser,)
	pagination_class = PageNumberPagination()
	def get(self, request):
		tags = Tag.objects.all()
		page = self.paginate_queryset(tags)
		if page is not None:
			serializer = self.get_paginated_response(TagSerializer(page,many=True).data)
		else:
			serializer = TagSerializer(tags, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	def post(self, request):
		serializer = TagSerializer(data=request.data)
		if serializer.is_valid():
			if uniqueName(request.data['name']) and uniqueSlug(request.data['slug']):
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			if not uniqueName(request.data['name']):
				errs['name'] = ["there is another tag with same name."]
			if not uniqueSlug(request.data['slug']):
				errs['slug'] = ["there is another tag with same slug."]
			return Response(errs,status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagView(APIView):
	def get_tag(self, slug):
		try:
			return Tag.objects.get(slug=slug)
		except:
			raise Http404
	
	def get(self, request, slug):
		tag = self.get_tag(slug)
		serializer = TagSerializer(tag)
		return Response(serializer.data, status=status.HTTP_200_OK)
	def put(self, request, slug):
		tag = self.get_tag(slug)
		serializer = TagSerializer(tag, request.data)
		if serializer.is_valid():
			if uniqueName(request.data['name'],tag.id) and uniqueSlug(request.data['slug'],tag.id):
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			if not uniqueName(request.data['name'],tag.id):
				errs['name'] = ["there is another tag with same name."]
			if not uniqueSlug(request.data['slug'],tag.id):
				errs['slug'] = ["there is another tag with same slug."]
			return Response(errs,status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, slug):
		tag = self.get_tag(slug)
		tag.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)