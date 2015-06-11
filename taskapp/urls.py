from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'clear-complete/$', views.clear_complete, name='clear_complete'),
    url(r'(?P<task_id>[0-9]+)/toggle-complete/$', views.toggle_complete, name='toggle_complete')
]
