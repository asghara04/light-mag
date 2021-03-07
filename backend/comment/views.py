from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment, Reply
from .serializer import CommentSerializer, MCommentSerializer, ReplySerializer, MReplySerializer
from django.http import Http404
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import AllowAny


class ACommentsView(APIView):
	permission_classes = (AllowAny,)
	def get(self, request, pk):
		comments = Comment.published.filter(article=pk)
		serializer = CommentSerializer(comments, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	def post(self, request, pk):
		request.data["article"] = pk
		serializer = CommentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"message":"نظرتون با موفقیت ثبت شد.\nپس از تایید نمایش داده میشود."}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CRepliesView(APIView):
	permission_classes = (AllowAny,)
	def get(self, request, pk):
		replies = Reply.published.filter(comment=pk)
		serializer = ReplySerializer(replies, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	def post(self, request, pk):
		serializer = ReplySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)