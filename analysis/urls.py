from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^common_follow/$', views.common_follow_form, name='common_follow_form'),
    url(r'^common_fav/$', views.common_fav_form, name='common_fav_form'),
    url(r'^common_rt/$', views.common_rt_form, name='common_rt_form'),
]
