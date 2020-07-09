from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^nav1/$', views.nav1, name="nav1"),

    url(r'^roster/$', views.roster, name="roster"),
    url(r'^rosterq/$', views.rosterq, name="rosterq"),

    url(r'^members/$', views.members, name="members"),
    url(r'^insertmems/$', views.insertmems, name="insertmems"),
    url(r'^deletemems/$', views.deletemems, name="deletemems"),
    url(r'^updatemems/$', views.updatemems, name="updatemems"),

    url(r'^scheduling/$', views.scheduling, name="schedule"),

    url(r'^material/$', views.material, name="materials"),
    url(r'^insertmats/$', views.insertmats, name="insertmats"),
    url(r'^deletemats/$', views.deletemats, name="deletemats"),
    url(r'^updatemats/$', views.updatemats, name="updatemats"),

    url(r'^car/$', views.car, name="car"),

    url(r'^powmech/$', views.powmech, name="power mechanism"),
    url(r'^powmechq/$', views.powmechq, name="power mechanism q"),

    url(r'^trial/$', views.trial, name="trials"),

    url(r'^stopmech/$', views.stopmech, name="stop mechanism"),
    url(r'^stopmechq/$', views.stopmechq, name="stop mechanism q"),
]