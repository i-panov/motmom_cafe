from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.getMostPopular),
    url(r'^(?P<pk>[0-9]+)/$', views.getCategory)
]
