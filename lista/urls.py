from django.conf.urls import url
from django.conf.urls import handler404
from . import views

handler404 = 'my_app.views.page_not_found'

urlpatterns = [
    url(r'^$', views.items_list, name='items_list'),
    url(r'^items/(?P<choice>\w{0,50})', views.items_list, name='items_list_select'),
    url(r'^donate/(?P<pk>[0-9]+)',views.donate,name='donor'),
    url(r'^info',views.info,name='info'),
]