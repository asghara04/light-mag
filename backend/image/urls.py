from django.urls import path
from .views import ImagesView, ImageView

urlpatterns = [
	path("mapi/v1/", ImagesView.as_view()),
	path("mapi/v1/<int:pk>", ImageView.as_view())
]