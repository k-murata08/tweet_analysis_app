from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^account/add/$', views.account_add, name='account_add'),
    url(r'^account/add/(?P<screen_name>[\w\-]+)/$', views.account_confirm, name='account_confirm'),
    url(r'^oauth/add/$', views.oauth_add, name='oauth_add'),

]
