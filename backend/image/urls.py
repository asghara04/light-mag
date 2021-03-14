from django.urls import path
from .views import ImagesView, ImagesCountView, ImageView

urlpatterns = [
	path("mapi/v1/", ImagesView.as_view()),
	path("mapi/v1/count/", ImagesCountView.as_view()),
	path("mapi/v1/<int:pk>/", ImageView.as_view())
]