from django.contrib import admin
from django.urls import path, include
from .views import redirect_blog

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', redirect_blog),
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('resume/', include('resume.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
