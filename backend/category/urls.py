from django.urls import path
from .views import CategoriesView, CategoryView, AllCatsView, SubCatsCatView

urlpatterns = [
	path("all/api/v1/", AllCatsView.as_view()),
	path("api/v1/", CategoriesView.as_view()),
	# subvats...
	path("api/v1/<slug:slug>/", CategoryView.as_view()),
	path("subs/api/v1/<int:pk>/", SubCatsCatView.as_view()),
]