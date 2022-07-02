"""drone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drones import urls as drones_urls_v1
from drones.v2 import urls as drones_urls_v2
from rest_framework import urls as rest_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/api',include(drones_urls_v1) ),
    path('v1/api-auth/',include(rest_urls)),
    path('v2/api',include(drones_urls_v2)),
    path('v2/api-auth/',include(rest_urls)),
]
