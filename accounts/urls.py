from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^account/add/$', views.account_add, name='account_add'),
    url(r'^account/confirm/$', views.account_confirm, name='account_confirm'),
]
