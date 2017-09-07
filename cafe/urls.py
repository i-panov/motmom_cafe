from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.most_popular),
    url(r'^(?P<pk>[0-9]+)/$', views.category),
    url(r'^cart/$', views.cart),
]
