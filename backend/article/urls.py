from django.urls import path
from .views import ArticlesView,ArticlesCountView,ArticleView,MArticlesView,MArticleView,CatArticlesView,SubCatArticlesView,LastArticlesView,MostComArticleView,TagArtsView
urlpatterns = [
	path("api/v1/", ArticlesView.as_view()),
	path("api/v1/count/", ArticlesCountView.as_view()),
	path("api/v1/lasts/", LastArticlesView.as_view()),
	path("api/v1/<slug:slug>/", ArticleView.as_view()),
	path("mapi/v1/", MArticlesView.as_view()),
	path("mapi/v1/<int:pk>/", MArticleView.as_view()),
	path("most/api/v1/comment/", MostComArticleView.as_view()),
	path("cat/api/v1/<int:pk>/", CatArticlesView.as_view()),
	path("cat/sub/api/v1/<int:pk>/", SubCatArticlesView.as_view()),
	path("tag/api/v1/<str:tag>/",TagArtsView.as_view())
]