from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^account/add/$', views.account_add, name='account_add'),
]
