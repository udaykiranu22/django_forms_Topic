"""
URL configuration for django_forms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact, name = 'contact'),
    path('Display_Topic/', Display_Topic, name = 'Display_Topic'),
    path('Display_Webpage/', Display_Webpage, name = 'Display_Webpage'),
    path('Display_AccessRecord/', Display_AccessRecord, name = 'Display_AccessRecord'),
    path('update_webpage/',update_webpage,name='update_webpage'),
]
