from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^nav1/$', views.nav1, name="nav1"),
   
    url(r'^roster/$', views.roster, name="roster"),
    url(r'^insertroster/', views.insertroster, name="insertroster"),
    url(r'^deleteroster/', views.deleteroster, name="deleteroster"),
    url(r'^updateroster/', views.updateroster, name="updateroster"),

    url(r'^members/$', views.members, name="members"),
    url(r'^insertmems/', views.insertmems, name="insertmems"),
    url(r'^deletemems/', views.deletemems, name="deletemems"),
    url(r'^updatemems/', views.updatemems, name="updatemems"),

    url(r'^scheduling/$', views.scheduling, name="schedule"),
    url(r'^insertsched/', views.insertsched, name="insertsched"),
    url(r'^deletesched/', views.deletesched, name="deletesched"),
    url(r'^updatesched/', views.updatesched, name="updatesched"),
    
    url(r'^material/$', views.material, name="materials"),
   
    url(r'^car/$', views.car, name="car"),
    
    url(r'^powmech/$', views.powmech, name="power mechanism"),
    url(r'^insertpows/', views.insertpows, name="insertpows"),
    url(r'^deletepows/', views.deletepows, name="deletepows"),
    
    
    url(r'^trial/$', views.trial, name="trials"),
    url(r'^inserttrial/', views.inserttrial, name="inserttrial"),
    url(r'^deletetrial/', views.deletetrial, name="deletetrial"),
    
    url(r'^stopmech/$', views.stopmech, name="stop mechanism"),
    url(r'^insertstops/', views.insertstops, name="insertstops"),
    url(r'^deletestops/', views.deletestops, name="deletestops"),
    
]
