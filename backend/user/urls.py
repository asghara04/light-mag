from django.urls import path, include
from .views import UserView, MUsersView, MUserView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
	path("api/v1/<str:uname>/", UserView.as_view()),
	path("auth/obtain_token/", obtain_jwt_token),
	path("auth/refresh_token/", refresh_jwt_token),
	path("auth/verify_token/", verify_jwt_token),
	path("mapi/v1/", MUsersView.as_view()),
	path("mapi/v1/<str:uname>/", MUserView.as_view())
]