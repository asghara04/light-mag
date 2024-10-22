from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Article
from .serializer import ArticleSerializer, MArticleSerializer, MinArticleSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination
from lightmag.pagination import PaginationMixin
from rest_framework.renderers import JSONRenderer
from django.db.models import Count,Q
from tag.models import Tag
import operator
from functools import reduce

from django.core.exceptions import FieldError


def search_in_articles(q, arts):
	return arts.filter(Q(title__icontains=q) | (Q(description__icontains=q) & Q(body__icontains=q))).order_by("title")


# ---- version 2 Classes and Views ----
# articles query
class ArticlesQueryView(APIView, PaginationMixin):
	pagination_class = PageNumberPagination()

	def get(self, request):
		# filters
		filters = dict(request.GET.copy())

		# cutting q
		if "q" in filters:
			q = filters.pop("q")

		# setting types
		for i in filters:
			try:
				filters[i] = int(filters[i][-1])
			except:
				return Response({"message":"please enter valid filters!"}, status=status.HTTP_400_BAD_REQUEST)

		# query
		try:
			articles = Article.published.filter(**filters)
		except:
			articles = Article.published.all()

		# searching in results
		if "q" in request.GET and q:
			q = q[-1]
			articles = search_in_articles(q, articles)

		# serializing the results
		page = self.paginate_queryset(articles)
		if page is not None:
			serializer = self.get_paginated_response(MinArticleSerializer(page, many=True, context={"request":request}).data)
		else:
			serializer = MinArticleSerializer(articles, many=True, context={"request":request})

		return Response(serializer.data, status=status.HTTP_200_OK)


# most commented articles from 1 to i
class MostComArticleViewI(APIView):
	def get(self, request):
		# setting i
		i = request.GET.get("i") or 6

		# query and sorting
		articles = Article.published.annotate(coms=Count('comments',filter=Q(comments__status=True,comments__personal=False))).order_by('-coms')[:int(i)]

		# serializing
		serializer = MinArticleSerializer(articles, many=True, context={"request":request})

		return Response(serializer.data,status=status.HTTP_200_OK)


# ---- version 1 Classes and Views ----
class ArticlesView(APIView, PaginationMixin):
	pagination_class = PageNumberPagination()
	renderer_classes = (JSONRenderer,)
	def get(self, request):
		arts = Article.published.all()
		if request.GET.get('q'):
			q = request.GET.get('q')
			arts = search_in_articles(q, arts)
		else:
			return Response({"message":"Enter somthing to search please."},status=status.HTTP_400_BAD_REQUEST)
		page = self.paginate_queryset(arts)
		if page is not None:
			serializer = self.get_paginated_response(MinArticleSerializer(page, many=True, context={"request":request}).data)
		else:
			serializer = MinArticleSerializer(arts, many=True, context={"request":request})

		return Response(serializer.data, status=status.HTTP_200_OK)


class ArticlesCountView(APIView):
	renderer_classes = (JSONRenderer,)
	def get(self, request, format=None):
		art_count = Article.published.all().count()
		content = {'count': art_count}
		return Response(content, status=status.HTTP_200_OK)


class LastArticlesView(APIView):
	renderer_classes = (JSONRenderer,)
	def get(self,request,format=None):
		arts = Article.published.all()[:6]
		serializer = MinArticleSerializer(arts, many=True, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleView(APIView):
	renderer_classes = (JSONRenderer,)
	def get_art(self, slug):
		try:
			return Article.published.get(slug=slug)
		except:
			raise Http404
	
	def get(self, request, slug):
		art = self.get_art(slug)
		serializer = ArticleSerializer(art, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)

errs = {'title':[],'slug':[]}
def uniqueTitle(title,pk=False):
	for art in Article.objects.all():
		if(not pk and art.title==title) or (pk and art.id!=pk and art.title==title):
			return False
	return True
def uniqueSlug(slug,pk=False):
	for art in Article.objects.all():
		if(not pk and art.slug==slug) or (pk and art.id!=pk and art.slug==slug):
			return False
	return True


class MArticlesView(APIView,PaginationMixin):
	pagination_class = PageNumberPagination()
	permission_classes = (IsAdminUser,)
	renderer_classes = (JSONRenderer,)
	def get(self, request):
		arts = Article.objects.all()
		page = self.paginate_queryset(arts)
		if page is not None:
			serializer = self.get_paginated_response(MArticleSerializer(page,many=True,context={"request":request}).data)
		else:
			serializer = MArticleSerializer(arts,many=True,context={"request":request})
		return Response(serializer.data,status=status.HTTP_200_OK)
	def post(self, request):
		serializer = MArticleSerializer(data=request.data, partial=True, context={"request":request})
		if serializer.is_valid():
			if uniqueTitle(request.data['title']) and uniqueSlug(request.data['slug']):
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			if not uniqueTitle(request.data['title']):
				errs['title'] = ['there is another article with same title.']
			if not uniqueSlug(request.data['slug']):
				errs['slug'] = ['there is another article with same slug.']
			return Response(errs,status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MArticleView(APIView):
	permission_classes = (IsAdminUser,)
	renderer_classes = (JSONRenderer,)
	def get_art(self, pk):
		try:
			return Article.objects.get(id=pk)
		except:
			raise Http404

	def get(self, request, pk):
		art = self.get_art(pk)
		serializer = MArticleSerializer(art, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	def patch(self, request, pk):
		art = self.get_art(pk)
		serializer = MArticleSerializer(art, request.data, partial=True, context={"request":request})
		if serializer.is_valid():
			if (not 'title' in request.data or ('title' in request.data and uniqueTitle(request.data['title'],art.id))) and (not 'slug' in request.data or ('slug' in request.data and uniqueSlug(request.data['slug'],art.id))):
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			if 'title' in request.data and not uniqueTitle(request.data['title'],art.id):
				errs['title'] = ['there is another article with same title.']
			if 'slug' in request.data and not uniqueSlug(request.data['slug'],art.id):
				errs['slug'] = ['there is another article with same slug.']
			return Response(errs,status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, pk):
		art = self.get_art(pk)
		art.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class CatArticlesView(APIView, PaginationMixin):
	pagination_class = PageNumberPagination()
	renderer_classes = (JSONRenderer,)
	def get(self, request, pk):
		arts = Article.published.filter(category=pk)
		page = self.paginate_queryset(arts)
		if page is not None:
			serializer = self.get_paginated_response(MinArticleSerializer(page, many=True, context={"request":request}).data)
		else:
			serializer = MinArticleSerializer(arts, many=True, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)


class SubCatArticlesView(APIView, PaginationMixin):
	pagination_class = PageNumberPagination();
	renderer_classes = (JSONRenderer,)
	def get(self, request, pk):
		arts = Article.published.filter(subcat=pk)
		page = self.paginate_queryset(arts)
		if page is not None:
			serializer = self.get_paginated_response(MinArticleSerializer(page, many=True, context={"request":request}).data)
		else:
			serializer = MinArticleSerializer(arts, many=True, context={"request":request})

		return Response(serializer.data, status=status.HTTP_200_OK)


class MostComArticleView(APIView):
	renderer_classes = (JSONRenderer,)
	def get(self,request,format=None):
		arts = Article.published.annotate(coms=Count('comments',filter=Q(comments__status=True,comments__personal=False))).order_by('-coms')[:7]
		serializer = MinArticleSerializer(arts, many=True, context={"request":request})
		return Response(serializer.data,status=status.HTTP_200_OK)

class TagArtsView(APIView,PaginationMixin):
	renderer_classes = (JSONRenderer,)
	pagination_class = PageNumberPagination()
	def getter(self,tag):
		try:
			return Tag.objects.get(slug=tag)
		except:
			raise Http404
	def get(self,request,tag,format=None):
		tag = self.getter(tag)
		arts = Article.published.filter(tags__in=[tag])
		page = self.paginate_queryset(arts)
		if page is not None:
			serializer = self.get_paginated_response(MinArticleSerializer(page,many=True,context={"request":request}).data)
		else:
			serializer = MinArticleSerializer(arts,many=True,context={"request":request})
		return Response(serializer.data,status=status.HTTP_200_OK)

class UserArtsView(APIView,PaginationMixin):
	pagination_class = PageNumberPagination()
	renderer_classes = (JSONRenderer,)
	def get(self,request,uname):
		arts = Article.published.filter(author__username=uname)
		page = self.paginate_queryset(arts)
		if page is not None:
			serializer = self.get_paginated_response(MinArticleSerializer(page,many=True,context={"request":request}).data)
		else:
			serializer = MinArticleSerializer(arts,many=True,context={"request":request})
		return Response(serializer.data,status=status.HTTP_200_OK)


class RelArts(APIView):
	renderer_classes = (JSONRenderer,)
	def getter(self, pk):
		try:
			return Article.published.get(id=pk)
		except:
			raise Http404

	def get(self, request, pk):
		art = self.getter(pk)
		n = 6

		if art.subcat:
			rel_arts = Article.published.filter(subcat__name=art.subcat.name)[:n]
		elif art.category:
			rel_arts = Article.published.filter(category__name=art.category.name)[:n]
		elif art.tags.count():
			rel_arts = Article.published.annotate(Count("tags"))[:n]
		else:
			title = art.title.split(" ")
			rel_arts = Article.published.filter(reduce(operator.and_, (Q(title__contains=word) for word in title)))[:n]

		rel_arts = list(filter(lambda i: i.id!=art.id, rel_arts))

		serializer = MinArticleSerializer(rel_arts, many=True, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)