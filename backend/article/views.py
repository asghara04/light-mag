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

class ArticlesView(APIView, PaginationMixin):
	pagination_class = PageNumberPagination()
	renderer_classes = (JSONRenderer,)
	def get(self, request):
		if not request.GET.get('q'):
			arts = Article.published.all()
		else:
			q = request.GET.get('q')
			arts = Article.published.filter(Q(title__icontains=q) | (Q(description__icontains=q) & Q(body__icontains=q))).order_by("title")
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


class MArticlesView(APIView):
	permission_classes = (IsAdminUser,)
	renderer_classes = (JSONRenderer,)
	def get(self, request):
		arts = Article.objects.all()
		serializer = MinArticleSerializer(arts, many=True, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	def post(self, request):
		serializer = MArticleSerializer(data=request.data, partial=True, context={"request":request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
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
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
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
		arts = Article.published.annotate(coms=Count('comments',filter=Q(comments__status=True,comments__personal=False))).order_by('-coms')[:6]
		serializer = MinArticleSerializer(arts, many=True, context={"request":request})
		return Response(serializer.data,status=status.HTTP_200_OK)