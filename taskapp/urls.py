from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'add/$', views.add, name='add'),
    url(r'delete/$', views.clear, name='delete'),
    url(r'^toggle_complete/(?P<task_id>[0-9]+)/$',views.toggle_complete, name='toggle_complete')
]
