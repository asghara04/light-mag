from django.urls import path
from .views import CategoriesView, CategoryView, AllCatsView, SubsCatCatView, SubCatView

urlpatterns = [
	path("all/api/v1/", AllCatsView.as_view()),
	path("api/v1/", CategoriesView.as_view()),
	path("sub/api/v1/<slug:slug>/", SubCatView.as_view()),
	path("api/v1/<slug:slug>/", CategoryView.as_view()),
	path("subs/api/v1/<int:pk>/", SubsCatCatView.as_view()),
]