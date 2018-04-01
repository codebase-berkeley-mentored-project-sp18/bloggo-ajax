from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^details/(?P<pk>\d+)$', views.post_details, name='post_details'),
]
