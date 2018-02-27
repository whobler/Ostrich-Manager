"""ostrich_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ostrich_app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^breeders/$', Breeders.as_view(), name='breeders'),
    # url(r'babies^/$', Babies.as_view(), name='babies'),
    # url(r'^eggs/$', Eggs.as_view(), name='eggs'),
    # url(r'^warehouse/$', Warehouse.as_view(), name='warehouse'),
    # url(r'^sold_birds/$', SoldBirds.as_view(), name='sold_birds'),
    # url(r'^budget/$', Budget.as_view(), name='budget'),
    # url(r'^seasons_statistics/$', SeasonsStatistics.as_view(), name='seasons_statistics'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutUser.as_view(), name='logout'),
]
