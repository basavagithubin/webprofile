from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from profileapp.views import profile

urlpatterns = [
    path("", profile, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
