from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment, Reply
from .serializer import CommentSerializer, MCommentSerializer, ReplySerializer, MReplySerializer
from django.http import Http404
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from lightmag.pagination import PaginationMixin
from rest_framework.pagination import PageNumberPagination

class ACommentsView(APIView,PaginationMixin):
	permission_classes = (AllowAny,)
	renderer_classes = (JSONRenderer,)
	pagination_class = PageNumberPagination()
	def get(self, request, pk):
		comments = Comment.published.filter(article=pk)
		page = self.paginate_queryset(comments)
		if page is not None:
			serializer = self.get_paginated_response(CommentSerializer(page,many=True).data)
		else:
			serializer = CommentSerializer(comments,many=True)
		return Response(serializer.data,status=status.HTTP_200_OK)
	def post(self, request, pk):
		serializer = CommentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"message":"نظرتون با موفقیت ثبت شد.\nپس از تایید نمایش داده میشود."}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CRepliesView(APIView,PaginationMixin):
	permission_classes = (AllowAny,)
	renderer_classes = (JSONRenderer,)
	pagination_class = PageNumberPagination()
	def get(self, request, pk):
		replies = Reply.published.filter(comment=pk)
		page = self.paginate_queryset(replies)
		if page is not None:
			serializer = self.get_paginated_response(ReplySerializer(page,many=True).data)
		else:
			serializer = ReplySerializer(replies,many=True)
		return Response(serializer.data,status=status.HTTP_200_OK)
	def post(self, request, pk):
		serializer = ReplySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)