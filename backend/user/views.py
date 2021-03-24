from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer, MUserSerializer, MinUserSerializer
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
	for user in User.objects.all():
		if (not pk and user.email==email) or (pk and user.email==email!=None and user.id!=pk):
			return False
	return True
def unique_username(username,pk=False):
	for user in User.objects.all():
		if (not pk and user.username==username) or (pk and user.id!=pk and user.username==username!=None):
			return False
	return True
def unique_pubmail(pub,pk=False):
	for user in User.objects.all():
		if (not pk and user.pubmail==pub) or (pk and user.id!=pk and user.pubmail==pub!=None):
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
			if unique_email(request.data['email']) and unique_username(request.data['username']) and (('pubmail' in request.data and unique_pubmail(request.data['pubmail'])) or not 'pubmail' in request.data):
				serializer.save()
				return Response({"message":"کاربر جدید با موفقیت ثبت شد."}, status=status.HTTP_201_CREATED)
			if not unique_email(request.data['email']):
				errs['email'] = ['کاربر دیگری با همین ایمیل وجود دارد.']
			if not unique_username(request.data['username']):
				errs['username'] = ['کاربر دیگری با همین نام کاربری وجود دارد.']
			if 'pubmail' in request.data and not unique_pubmail(request.data['pubmail']):
				errs['pubmail'] = ['کاربر دیگری با همین ایمیل عمومی وجود دارد.']
			return Response(errs,status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MUserView(APIView):
	permission_classes = (IsAdminUser,)
	renderer_classes = (JSONRenderer,)
	def get_user(self, uname):
		try:
			return User.objects.get(username=uname)
		except:
			raise Http404

	def get(self, request, uname):
		user = self.get_user(uname)
		serializer = MUserSerializer(user, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	def patch(self, request, uname):
		user = self.get_user(uname)
		serializer = MUserSerializer(user, request.data, partial=True, context={"request":request})
		if serializer.is_valid():
			if (not 'email' in request.data or('email' in request.data and unique_email(request.data['email'],user.id))) and (not 'username' in request.data or ('username' in request.data and unique_username(request.data['username'],user.id))) and (not 'pubmail' in request.data or ('pubmail' in request.data and unique_pubmail(request.data['pubmail'],user.id))):
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			if 'email' in request.data and not unique_email(request.data['email'],user.id):
				errs['email'] = ['کاربر دیگری با همین ایمیل وجود دارد!']
			if 'username' in request.data and not unique_username(request.data['username'],user.id):
				errs['username'] = ['کاربر دیگری با همین نام کاربری وجود دارد!']
			if 'pubmail' in request.data and not unique_pubmail(request.data['pubmail'],user.id):
				errs['pubmail'] = ['کاربر دیگری با همین ایمیل عمومی وجود دارد!']
			return Response(errs,status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, uname):
		user = self.get_user(uname)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class ActUsersView(APIView):
	permission_classes = (IsAdminUser,)
	def get(self, request):
		users = User.actives.all()
		serializer = MinUserSerializer(users,many=True)
		return Response(serializer.data,status=status.HTTP_200_OK)