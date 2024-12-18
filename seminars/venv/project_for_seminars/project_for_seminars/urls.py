"""
URL configuration for project_for_seminars project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_menu_1_1/', include('seminarapp_1_1.urls')),
    path('main_menu_1_2/', include('seminarapp_1_2.urls')),
    path('main_menu_hw_1/', include('hw_seminar_1.urls')),
    path('main_menu_2_1/', include('seminarapp_2_1.urls')),
    path('main_menu_hw_2/', include('hw_seminar_2.urls')),
    path('main_menu_3_1/', include('seminarapp_3_1.urls')),
    path('main_menu_hw_3/', include('hw_seminar_3.urls')),
    path('main_menu_4_1/', include('seminarapp_4_1.urls'), name='main_menu_4_1'),
    path('main_menu_hw_4/', include('hw_seminar_4.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
