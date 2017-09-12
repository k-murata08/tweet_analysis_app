from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^common_follow/$', views.common_follow_form, name='common_follow_form'),
    url(r'^common_follow/result/$', views.common_follow_result, name='common_follow_result'),
    url(r'^common_follow/result/(?P<pk>[0-9]+)/$', views.common_follow_result_detail, name='common_follow_result_detail'),
    url(r'^common_fav/$', views.common_fav_form, name='common_fav_form'),
    url(r'^common_fav/result/$', views.common_fav_result, name='common_fav_result'),
    url(r'^common_fav/result/(?P<pk>[0-9]+)/$', views.common_fav_result_detail, name='common_fav_result_detail'),
    url(r'^common_rt/$', views.common_rt_form, name='common_rt_form'),
    url(r'^common_rt/result/$', views.common_rt_result, name='common_rt_result'),
    url(r'^common_rt/result/(?P<pk>[0-9]+)/$', views.common_rt_result_detail, name='common_rt_result_detail'),
]
