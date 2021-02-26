from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Article
from .serializer import ArticleSerializer, MArticleSerializer, MinArticleSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination
from lightmag.pagination import PaginationMixin

class ArticlesView(APIView, PaginationMixin):
	pagination_class = PageNumberPagination()

	def get(self, request):
		arts = Article.published.all()
		page = self.paginate_queryset(arts)
		if page is not None:
			serializer = self.get_paginated_response(MinArticleSerializer(page, many=True, context={"request":request}).data)
		else:
			serializer = MinArticleSerializer(arts, many=True, context={"request":request})

		return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleView(APIView):
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

class CatArticlesView(APIView):
	def get(self, request, pk):
		arts = Article.published.filter(category=pk)
		serializer = MinArticleSerializer(arts, many=True, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)