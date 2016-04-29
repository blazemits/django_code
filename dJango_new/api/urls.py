from django.conf.urls import patterns, url
from api.views import test,task_detail,task_list

urlpatterns = patterns('',
    url(r'^test/$', test),
    url(r'^tasks/([a-zA-Z]+)$',task_list,name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$',task_detail,name='task_detail'),
    )