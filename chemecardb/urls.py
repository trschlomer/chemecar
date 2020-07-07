from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^nav1/$', views.nav1, name="nav1"),
    url(r'^roster/$', views.roster, name="roster"),
    url(r'^members/$', views.members, name="members"),
    url(r'^scheduling/$', views.scheduling, name="schedule"),
    url(r'^material/$', views.material, name="materials"),
    url(r'^car/$', views.car, name="car"),
    url(r'^powmech/$', views.powmech, name="power mechanism"),
    url(r'^trial/$', views.trial, name="trials"),
    url(r'^stopmech/$', views.stopmech, name="stop mechanism"),
]