from django.conf.urls import url
from . import views

urlpatterns = [
    # /firstApp
    url(r'^$', views.index, name='index'),
    # /firstApp/5
    url(r'^(?P<questionID>[0-9]+)/$', views.detail, name='detail'),
    # /firstApp/5/results/
    url(r'^(?P<questionID>[0-9]+)/results/$', views.results, name='results'),
    # /firstApp/5/vote/
    url(r'^(?P<questionID>[0-9]+)/vote/$', views.vote, name='vote')
]
