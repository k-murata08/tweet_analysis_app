from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^common_follow/$', views.common_follow_form, name='common_follow_form')
]
