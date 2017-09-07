from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.get_most_popular),
    url(r'^(?P<pk>[0-9]+)/$', views.get_category)
]
