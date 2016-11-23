from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process/$', views.process, name='process'),
    url(r'^impact/$', views.impact, name='impact'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^test/$', views.test, name='test'),
]
