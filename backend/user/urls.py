from django.urls import path, include
from .views import UserView, MUsersView, MUserView,ActUsersView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
	path("api/v1/<slug:uname>/", UserView.as_view()),
	path("auth/obtain_token/", obtain_jwt_token),
	path("auth/refresh_token/", refresh_jwt_token),
	path("auth/verify_token/", verify_jwt_token),
	path("mapi/v1/", MUsersView.as_view()),
	path("mapi/v1/<slug:uname>/", MUserView.as_view()),
	path("acts/mapi/v1/",ActUsersView.as_view())
]