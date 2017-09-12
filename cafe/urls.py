from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'cafe'


urlpatterns = [
    url(r'^$', views.most_popular, name='most_popular'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^cart/$', TemplateView.as_view(template_name='cafe/cart.html'), name='cart'),
    url(r'^cart/render/$', views.render_cart, name='render_cart')
]
