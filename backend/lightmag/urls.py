from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path("images/", include("image.urls")),
	path("categories/", include("category.urls")),
	path("users/", include('user.urls')),
	path("tags/", include('tag.urls')),
	path("articles/", include('article.urls')),
	path("comments/", include("comment.urls")),
	path("rest_auth/mapi/", include("rest_framework.urls")),
	path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)