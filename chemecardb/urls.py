from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^nav1/$', views.nav1, name="nav1"),
    url(r'^roster/$', views.roster, name="roster"),
    url(r'^members/$', views.members, name="members"),
    url(r'^schedule/$', views.schedule, name="schedule"),
    url(r'^materials/$', views.materials, name="materials"),
    url(r'^car/$', views.car, name="car"),
    url(r'^powmech/$', views.powmech, name="powmech"),
    url(r'^trials/$', views.trials, name="trials"),
    url(r'^stopmech/$', views.stopmech, name="stopmech"),
]