"""
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("taks/", include('taks.urls')),
    path("produto/", include('produto.urls')),
    path("sobre/", include('sobre.urls')),
]
