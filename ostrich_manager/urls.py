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

    url(r'^get_breeder/(?P<id>\d+)/$', GetBreeder.as_view(), name='get_breeder'),
    url(r'^get_breeders/$', GetBreeders.as_view(), name='get_breeders'),
    url(r'^breeders/$', Breeders.as_view(), name='breeders'),
    url(r'^show_breeders/$', ShowBreeders.as_view(), name='show_breeders'),
    url(r'^add_breeder/$', AddBreeder.as_view(), name='add_breeder'),
    url(r'^modify_breeder/(?P<id>\d+)/$', ModifyBreeder.as_view(), name='modify_breeder'),

    url(r'^get_eggs_baby/(?P<id>\d+)/$', GetEggsBaby.as_view(), name='get_eggs_babies'),
    url(r'^get_eggs_babies/$', GetEggsBabies.as_view(), name='get_eggs_babies'),
    url(r'^eggs_babies/$', ShowEggsBabies.as_view(), name='eggs_babies'),

    url(r'^warehouse/$', ShowWarehouse.as_view(), name='show_warehouse'),

    url(r'^sold_birds/$', ShowSoldBirds.as_view(), name='show_sold_birds'),

    url(r'^budget/$', ShowBudget.as_view(), name='show_budget'),

    url(r'^seasons_statistics/$', ShowSeasonsStatistics.as_view(), name='show_seasons_statistics'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutUser.as_view(), name='logout'),
]
