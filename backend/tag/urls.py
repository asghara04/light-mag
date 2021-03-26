from django.urls import path
from .views import TagView, TagsView

urlpatterns = [
	path("mapi/v1/", TagsView.as_view()),
	path("api/v1/<str:slug>/", TagView.as_view())
]