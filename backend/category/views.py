from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .models import Category, SubCat
from .serializer import AllCategorySerializer, CategorySerializer, SubCatSerializer
from rest_framework.pagination import PageNumberPagination
from lightmag.pagination import PaginationMixin
from rest_framework.renderers import JSONRenderer

errs = {'name':[],'slug':[]}

class AllCatsView(APIView):
	def get(self, request):
		cats = Category.objects.all()
		serializer = AllCategorySerializer(cats, many=True, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)

def unique_cat_name(name):
	for cat in Category.objects.all():
		if name==cat.name:
			return False
	return True

def unique_cat_slug(slug):
	for cat in Category.objects.all():
		if slug==cat.slug:
			return False
	return True

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
			if unique_cat_name(request.data['name']) and unique_cat_slug(request.data['slug']):
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			if not unique_cat_name(request.data['name']):
				errs['name'] = ["دسته دیگری با همین نام وجود دارد."]
			if not unique_cat_slug(request.data['slug']):
				errs['slug'] = ["دسته دیگری با همین اسلاگ وجود دارد."]
			return Response(errs, status=status.HTTP_400_BAD_REQUEST)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesCountView(APIView):
	renderer_classes = (JSONRenderer,)
	def get(self, request, format=None):
		cats_count = Category.objects.all().count()
		content = {'count': cats_count}
		return Response(content, status=status.HTTP_200_OK)


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



class SubsCatCatView(APIView, PaginationMixin):
	pagination_class = PageNumberPagination()
	def get(self, request, pk):
		subcats = SubCat.objects.filter(category=pk)
		page = self.paginate_queryset(subcats)
		if page is not None:
			serializer = self.get_paginated_response(SubCatSerializer(page, many=True, context={"request":request}).data)
		else:
			serializer = SubCatSerializer(subcats, many=True, context={"request":request})
		return Response(data=serializer.data, status=status.HTTP_200_OK)

	# post


class SubCatView(APIView):
	def getter(self, cat, sub):
		try:
			return SubCat.objects.get(category=cat, slug=sub)
		except:
			raise Http404

	def get(self, request, cat, sub):
		subcat = self.getter(cat, sub)
		serializer = SubCatSerializer(subcat, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)

	# put/patch
	# delete