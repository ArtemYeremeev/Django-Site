from django.contrib import admin
from django.urls import path, include
from .views import redirect_blog

urlpatterns = [
    path('', redirect_blog),
    path('admin/', admin.site.urls),
    path('main/', include('main.urls'))
]
