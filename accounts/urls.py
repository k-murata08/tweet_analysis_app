from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', views.logout_to_index, name='logout'),
    url(r'^user/add/$', views.user_add, name='user_add'),
    url(r'^account/add/$', views.account_add, name='account_add'),
    url(r'^account/add/(?P<screen_name>[\w\-]+)/$', views.account_confirm, name='account_confirm'),
    url(r'^account/del/$', views.account_del, name='account_del'),
    url(r'^oath/add/$', views.oath_add, name='oath_add'),
]
