from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^nav1/$', views.nav1, name="nav1"),
    url(r'^roster/$', views.roster, name="roster"),
    url(r'^schedule/$', views.schedule, name="schedule"),
    url(r'^materials/$', views.materials, name="materials"),
    url(r'^car/$', views.car, name="car"),
]