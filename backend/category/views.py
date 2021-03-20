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
	renderer_classes = (JSONRenderer,)
	def get(self, request):
		cats = Category.objects.all()
		serializer = AllCategorySerializer(cats, many=True, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)


def unique_cat_name(name,pk=False):
	if not pk:
		for cat in Category.objects.all():
			if name==cat.name:
				return False
		return True
	elif type(pk)==int and Category.objects.get(id=pk):
		for cat in Category.objects.all():
			if name==cat.name and pk!=cat.id:
				return False
		return True
	else:
		raise Http404
def unique_cat_slug(slug,pk=False):
	if not pk:
		for cat in Category.objects.all():
			if slug==cat.slug:
				return False
		return True
	elif type(pk)==int and Category.objects.get(id=pk):
		for cat in Category.objects.all():
			if slug==cat.slug and pk!=cat.id:
				return False
		return True
	else:
		raise Http404


class CategoriesView(APIView, PaginationMixin):
	renderer_classes = (JSONRenderer,)
	pagination_class = PageNumberPagination()
	def get(self, request):
		if request.GET.get('q') is None:
			cats = Category.objects.all()
		elif request.GET.get("q"):
			q = request.GET.get('q')
			cats = Category.objects.filter(name__icontains=q).order_by("name")
		else:
			return Response({"message":"لطفا کلمه ای ربای جستوجو وارد کنید."},status=status.HTTP_400_BAD_REQUEST)
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
	renderer_classes = (JSONRenderer,)
	def get_cat(self, slug):
		try:
			return Category.objects.get(slug=slug)
		except:
			raise Http404
	def get(self, request, slug):
		category = self.get_cat(slug)
		serializer = CategorySerializer(category, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	def patch(self, request, slug):
		category = self.get_cat(slug)
		serializer = CategorySerializer(category, request.data, partial=True, context={"request":request})
		if serializer.is_valid() and ('slug' in request.data or 'name' in request.data or 'image' in request.data):
			if (not 'slug' in request.data or('slug' in request.data and unique_cat_slug(request.data['slug'],category.id))) and (not 'name' in request.data or('name' in request.data and unique_cat_name(request.data['name'],category.id))):
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			if 'name' in request.data and not unique_cat_name(request.data['name'],category.id):
				errs['name'] = ["دسته دیگری با همین نام وجود دارد."]
			if 'slug' in request.data and not unique_cat_slug(request.data['slug'],category.id):
				errs['slug'] = ["دسته دیگری با همین اسلگ وجود دارد."]
			return Response(errs,status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
	def delete(self, request, slug):
		category = self.get_cat(slug)
		category.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


def uniqueSubCatName(catname,name,pk=False):
	for cat in Category.objects.get(name=catname).subcats.all():
		if (cat.name==name and not pk) or (pk and cat.name==name and cat.id!=pk):
			return False
	return True
def uniqueSubCatSlug(catname,slug,pk=False):
	for cat in Category.objects.get(name=catname).subcats.all():
		if (cat.slug==slug and not pk) or (pk and cat.slug==slug and cat.id!=pk):
			return False
	return True

class SubsCatCatView(APIView, PaginationMixin):
	renderer_classes = (JSONRenderer,)
	pagination_class = PageNumberPagination()
	def get(self, request, pk):
		subcats = SubCat.objects.filter(category=pk)
		page = self.paginate_queryset(subcats)
		if page is not None:
			serializer = self.get_paginated_response(SubCatSerializer(page, many=True, context={"request":request}).data)
		else:
			serializer = SubCatSerializer(subcats, many=True, context={"request":request})
		return Response(data=serializer.data, status=status.HTTP_200_OK)

	def post(self, request, pk):
		serializer = SubCatSerializer(data=request.data, partial=True, context={"request":request})
		if serializer.is_valid():
			if uniqueSubCatName(request.data['category'],request.data['name']) and uniqueSubCatSlug(request.data['category'],request.data['slug']):
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			if not uniqueSubCatName(request.data['category'],request.data['name']):
				errs['name'] = ['زیر دسته دیگری با همین نام در این دسته وجود دارد.']
			if not uniqueSubCatSlug(request.data['category'],request.data['slug']):
				errs['slug'] = ['زیر دسته دیگری با همین اسلاگ در این دسته وجود دارد.']
			return Response(errs, status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.permissions import AllowAny
class SubCatView(APIView):
	# renderer_classes = (JSONRenderer,)
	permission_classes = (AllowAny,)
	def getter(self, cat, sub):
		try:
			category = Category.objects.get(slug=cat)
			return category.subcats.get(slug=sub)
		except:
			raise Http404

	def get(self, request, cat, sub):
		subcat = self.getter(cat, sub)
		serializer = SubCatSerializer(subcat, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	def patch(self,request,cat,sub):
		subcat = self.getter(cat,sub)
		serializer = SubCatSerializer(subcat,request.data,partial=True,context={"request":request})
		if serializer.is_valid() and ('category' in request.data or 'image' in request.data or 'name' in request.data or 'slug' in request.data):
				if (not 'name' in request.data or ('name' in request.data and ((not 'category' in request.data and uniqueSubCatName(subcat.category,request.data['name'],subcat.id)) or ('category' in request.data and uniqueSubCatName(request.data['category'],request.data['name'],subcat.id))))) and (not 'slug' in request.data or ('slug' in request.data and ((not 'category' in request.data and uniqueSubCatSlug(subcat.category,request.data['slug'],subcat.id)) or ('category' in request.data and uniqueSubCatSlug(request.data['category'],request.data['slug'],subcat.id))))):
					serializer.save();
					return Response(serializer.data,status=status.HTTP_200_OK)
				if 'name' in request.data and ((not 'category' in request.data and uniqueSubCatName(subcat.category,request.data['name'],subcat.id)) or ('category' in request.data and uniqueSubCatName(request.data['category'],request.data['name'],subcat.id))):
					errs['name'] = ["زیردسته دیگری با همین نام در این دسته وجود دارد."]
				if 'slug' in request.data and ((not 'category' in request.data and uniqueSubCatSlug(subcat.category,request.data['slug'],subcat.id)) or ('category' in request.data and uniqueSubCatSlug(request.data['category'],request.data['slug'],subcat.id))):
					errs['slug'] = ["زیردسته دیگری با همین اسلاگ در این دسته وجود دارد."]
				return Response(errs,status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	def delete(self,request,cat,sub):
		subcat = self.getter(cat,sub)
		subcat.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)