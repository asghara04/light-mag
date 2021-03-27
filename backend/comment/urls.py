from django.urls import path
from .views import ACommentsView, CRepliesView,McommentsView,McommentView,MReplyView

urlpatterns = [
	path("api/v1/<int:pk>/", ACommentsView.as_view()),
	path("reply/api/v1/<int:pk>/", CRepliesView.as_view()),
	path("mapi/v1/",McommentsView.as_view()),
	path("mapi/v1/<int:pk>/",McommentView.as_view()),
	path("reply/mapi/v1/<int:pk>/", MReplyView.as_view())
]