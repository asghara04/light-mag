from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .models import Category, SubCat
from .serializer import CategorySerializer, SubCatSerializer
from rest_framework.pagination import PageNumberPagination
from lightmag.pagination import PaginationMixin


class AllCatsView(APIView):
	def get(self, request):
		cats = Category.objects.all()
		serializer = CategorySerializer(cats, many=True, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)


class CategoriesView(APIView, PaginationMixin):
	pagination_class = PageNumberPagination()
	def get(self, request):
		cats = Category.objects.all()
		page = self.paginate_queryset(cats)
		if page is not None:
			serializer = self.get_paginated_response(CategorySerializer(page, many=True, context={"request":request}).data)
		else:
			serializer = CategorySerializer(cats, many=True, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	def post(self, request):
		serializer = CategorySerializer(data=request.data, partial=True, context={"request":request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(APIView):
	def get_cat(self, slug):
		try:
			return Category.objects.get(slug=slug)
		except:
			raise Http404
	def get(self, request, slug):
		category = self.get_cat(slug)
		serializer = CategorySerializer(category, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	def put(self, request, slug):
		category = self.get_cat(slug)
		serializer = CategorySerializer(category, context={"request":request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status.HTTP_200_OK)
		return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
	def delete(self, request, slug):
		category = self.get_cat(slug)
		category.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



class SubCatsCatView(APIView, PaginationMixin):
	pagination_class = PageNumberPagination()
	def get(self, request, pk):
		subcats = SubCat.objects.filter(category=pk)
		page = self.paginate_queryset(subcats)
		if page is not None:
			serializer = self.get_paginated_response(SubCatSerializer(page, many=True, context={"request":request}).data)
		else:
			serializer = SubCatSerializer(subcats, many=True, context={"request":request})
		return Response(data=serializer.data, status=status.HTTP_200_OK)