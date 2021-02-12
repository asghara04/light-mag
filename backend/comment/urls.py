from django.urls import path
from .views import ACommentsView, CRepliesView

urlpatterns = [
	path("api/v1/<int:pk>/", ACommentsView.as_view()),
	path("reply/api/v1/<int:pk>/", CRepliesView.as_view()),
]