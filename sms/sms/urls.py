"""
URL configuration for sms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .import settings
from django.conf.urls.static import static
from sms_app import views, Hodviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', views.showDemoPage),
    path("", views.showLoginPage),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.log_out),
    path('doLogin', views.doLogin),
    path('admin_home', Hodviews.admin_home)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)