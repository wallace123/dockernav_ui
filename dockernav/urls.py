from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start_page, name='start_page'),
    url(r'^container/new/$', views.container_new, name='new_container'),
    url(r'^container/new/vnc/(?P<cont_pk>\d+)/navserver/(?P<nav_pk>\d+)/$', views.vnc_new, name='new_vnc'),
    url(r'^container/new/jabber/(?P<cont_pk>\d+)/navserver/(?P<nav_pk>\d+)/$', views.jabber_new, name='new_jabber'),
]
