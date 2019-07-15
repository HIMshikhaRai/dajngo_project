"""roomfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from rooms.views import home_template
from forms.views import renter_view,landlord_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_template,name="home_page"),
    path('renter/',renter_view),
    path('landlord/',landlord_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

 # urlpatterns += staticfiles_urlpatterns()
 # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
