from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer, MUserSerializer
from rest_framework.permissions import IsAdminUser
from django.http import Http404


class UserView(APIView):
	def get_user(self, uname):
		try:
			return User.objects.get(username=uname)
		except:
			raise Http404

	def get(self, request, uname):
		user = self.get_user(uname)
		print(user)
		serializer = UserSerializer(uname, context={"request":request})
		print(serializer.data)
		return Response(serializer.data, status=status.HTTP_200_OK)


class MUsersView(APIView):
	permission_classes = (IsAdminUser,)
	def get(self, request):
		users = User.objects.all()
		serializer = MUserSerializer(users, many=True, context={"request":request})
		return Response(serializer.data, status=status.HTTP_200_OK)
	def post(self, request):
		serializer = MUserSerializer(data=request.data, partial=True, context={"request":request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



class MUserView(APIView):
	permission_classes = (IsAdminUser,)
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