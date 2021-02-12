from django.urls import path
from .views import TagView, TagsView

urlpatterns = [
	path("api/v1", TagView.as_view()),
	path("api/v1/<int:pk>", TagView.as_view())
]