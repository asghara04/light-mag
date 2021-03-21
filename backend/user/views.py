from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer, MUserSerializer
from rest_framework.permissions import IsAdminUser
from django.http import Http404
from rest_framework.renderers import JSONRenderer
from lightmag.pagination import PaginationMixin
from rest_framework.pagination import PageNumberPagination

class UserView(APIView):
	renderer_classes = (JSONRenderer,)
	def get_user(self, uname):
		try:
			return User.objects.get(username=uname)
		except:
			raise Http404

	def get(self, request, uname):
		user = self.get_user(uname)
		serializer = UserSerializer(user, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)


errs = {"email":[],"username":[],"pubmail":[]}

def unique_email(email,pk=False):
	if not pk:
		for user in User.objects.all():
			if user.email==email:
				return False
		return True
def unqiue_username(username,pk=False):
	if not pk:
		for user in User.objects.all():
			if user.username==username:
				return False
		return True
def unique_pubmail(pub,pk=False):
	if not pk:
		for user in User.objects.all():
			if user.pubmail==pub:
				return False
		return True

class MUsersView(APIView,PaginationMixin):
	renderer_classes = (JSONRenderer,)
	permission_classes = (IsAdminUser,)
	pagination_class = PageNumberPagination()
	def get(self, request):
		users = User.objects.all()
		page = self.paginate_queryset(users)
		if page is not None:
			serializer = self.get_paginated_response(MUserSerializer(page,many=True,context={"request":request}).data)
		else:
			serializer = MUserSerializer(users, many=True, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	def post(self, request):
		serializer = MUserSerializer(data=request.data, partial=True, context={"request":request})
		if serializer.is_valid():
			if unique_email(request.data['email']) and unqiue_username(request.data['username']) and (('pubmail' in request.data and unique_pubmail(request.data['pubmail'])) or not 'pubmail' in request.data):
				serializer.save()
				return Response({"message":"کاربر جدید با موفقیت ثبت شد."}, status=status.HTTP_201_CREATED)
			if not unique_email(request.data['email']):
				errs['email'] = ['کاربر دیگری با همین ایمیل وجود دارد.']
			if not unqiue_username(request.data['username']):
				errs['username'] = ['کاربر دیگری با همین نام کاربری وجود دارد.']
			if 'pubmail' in request.data and unique_pubmail(request.data['pubmail']):
				errs['pubmail'] = ['کاربر دیگری با همین ایمیل عمومی وجود دارد.']
			return Response(errs,status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MUserView(APIView):
	permission_classes = (IsAdminUser,)
	renderer_classes = (JSONRenderer,)
	def get_user(self, pk):
		try:
			return User.objects.get(id=pk)
		except:
			raise Http404

	def get(self, request, pk):
		user = self.get_user(pk)
		serializer = MUserSerializer(user, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	def patch(self, request, pk):
		user = self.get_user(pk)
		serializer = MUserSerializer(user, request.data, partial=True, context={"request":request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, pk):
		user = self.get_user(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)