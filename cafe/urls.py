from django.conf.urls import url

from . import views


app_name = 'cafe'


urlpatterns = [
    url(r'^$', views.most_popular, name='most_popular'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^cart/$', views.cart, name='cart'),
]
