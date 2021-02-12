from django.urls import path
from .views import CategoriesView, CategoryView, AllCatsView

urlpatterns = [
	path("all/api/v1/", AllCatsView.as_view()),
	path("api/v1/", CategoriesView.as_view()),
	path("api/v1/<slug:slug>/", CategoryView.as_view())
]