from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('cinema.urls')),
    # path('', include('parser.urls')),
    path("accounts/", include("accounts.urls")), # new
    path("accounts/", include("django.contrib.auth.urls")), # new
    path("", TemplateView.as_view(template_name="home.html"),
    name="home"), # new
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)