from django.urls import path
from .views import ArticlesView, ArticleView, MArticlesView, MArticleView

urlpatterns = [
	path("api/v1/", ArticlesView.as_view()),
	path("api/v1/<slug:slug>/", ArticleView.as_view()),
	path("mapi/v1/", MArticlesView.as_view()),
	path("mapi/v1/<int:pk>/", MArticleView.as_view())
]