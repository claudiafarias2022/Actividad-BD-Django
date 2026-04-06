from django.contrib import admin
from django.urls import include, path

urlpatterns = [
path('', include('saludo.urls')),
path('admin/', admin.site.urls)
]

urlpatterns = [
path('admin/', admin.site.urls),
path('api/', include('app.urls')),
]