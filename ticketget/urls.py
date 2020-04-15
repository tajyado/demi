"""ticketget URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import myapp.views
urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
	path("", myapp.views.index, name='index'),
    path('admin/', admin.site.urls),
    path("index/", myapp.views.index, name='index'),
    path("spage/", myapp.views.spage, name='spage'),
    path("index/search/", myapp.views.search, name='search'),
    path("search/", myapp.views.search, name='search'),
    path("deletefavor/", myapp.views.deletefavor, name='search'),
    path("templates/2/", myapp.views.Aimer, name='Aimer'),
    path("templates/3/", myapp.views.Aska , name='Aska'),
    path("templates/6/", myapp.views.MorningGirl, name='MorningGirl'),
    path("templates/5/", myapp.views.XiaoBinZhe, name='XiaoBinZhe'),
    path("templates/9/", myapp.views.MAMAMOO, name='MAMAMOO'),
    path("templates/8/", myapp.views.BTS, name='BTS'),
    path("templates/10/", myapp.views.Shawn, name='Shawn'),
    path("templates/11/", myapp.views.WestLife, name='WestLife'),
    path("templates/13/", myapp.views.eight, name='eight'),
    path("templates/12/", myapp.views.BaiAn, name='BaiAn'),
    path("", include('myapp.urls')),
]
