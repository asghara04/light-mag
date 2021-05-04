from django.urls import path


from article.views import (

	# --- version 2 Classes ---
	ArticlesQueryView,

	# --- version 1 Classes ---
	ArticlesView,
	ArticlesCountView,
	ArticleView,
	RelArts,
	MArticlesView,
	MArticleView,
	CatArticlesView,
	SubCatArticlesView,
	LastArticlesView,
	MostComArticleView,
	TagArtsView,
	UserArtsView
)

urlpatterns = [
	# --- version 2 URLs ---
	path("api/v2/", ArticlesQueryView.as_view()),
	# --- version 1 URLs ---
	path("api/v1/", ArticlesView.as_view()),
	path("api/v1/count/", ArticlesCountView.as_view()),
	path("api/v1/lasts/", LastArticlesView.as_view()),
	path("api/v1/<slug:slug>/", ArticleView.as_view()),
	path("related/api/v1/<int:pk>/", RelArts.as_view()),
	path("mapi/v1/", MArticlesView.as_view()),
	path("mapi/v1/<int:pk>/", MArticleView.as_view()),
	path("most/api/v1/comment/", MostComArticleView.as_view()),
	path("cat/api/v1/<int:pk>/", CatArticlesView.as_view()),
	path("cat/sub/api/v1/<int:pk>/", SubCatArticlesView.as_view()),
	path("tag/api/v1/<str:tag>/",TagArtsView.as_view()),
	path("user/api/v1/<slug:uname>/",UserArtsView.as_view())
]