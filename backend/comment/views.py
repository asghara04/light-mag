from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment, Reply
from .serializer import CommentSerializer, MCommentSerializer, ReplySerializer, MReplySerializer
from django.http import Http404
from rest_framework.permissions import IsAdminUser,AllowAny
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
			return Response({"message":"your comment submitted successfully.\nit'll public after approved."}, status=status.HTTP_201_CREATED)
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
			return Response({"message":"your reply submitted successfully.\nit'll be public after approved."}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class McommentsView(APIView,PaginationMixin):
	pagination_class = PageNumberPagination()
	renderer_classes = (JSONRenderer,)
	permission_classes = (IsAdminUser,)
	def get(self,request):
		coms = Comment.objects.all()
		page = self.paginate_queryset(coms)
		if page is not None:
			serializer = self.get_paginated_response(MCommentSerializer(page,many=True).data)
		else:
			serializer = self.get_paginated_response(MCommentSerializer(coms,many=True))
		return Response(serializer.data,status=status.HTTP_200_OK)


class McommentView(APIView):
	permission_classes = (IsAdminUser,)
	def getter(self, pk):
		try:
			return Comment.objects.get(id=pk)
		except:
			raise Http404
	def get(self,request,pk):
		com = self.getter(pk)
		serializer = MCommentSerializer(com)
		return Response(serializer.data, status=status.HTTP_200_OK)
	def put(self, request, pk):
		com = self.getter(pk)
		serializer = MCommentSerializer(com, request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_200_OK)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, pk):
		com = self.getter(pk)
		com.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class MReplyView(APIView):
	permission_classes = (IsAdminUser,)
	def getter(self,pk):
		try:
			return Reply.objects.get(id=pk)
		except:
			raise Http404
	def get(self, request, pk):
		com = self.getter(pk)
		serializer = MReplySerializer(com)
		return Response(serializer.data,status=status.HTTP_200_OK)
	def put(self, request, pk):
		rep = self.getter(pk)
		serializer = MReplySerializer(rep, request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_200_OK)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)			
	def delete(self, request, pk):
		rep = self.getter(pk)
		rep.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)