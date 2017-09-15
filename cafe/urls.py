from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'cafe'


urlpatterns = [
    url(r'^$', views.MostPopularView.as_view(), name='most_popular'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^cart/$', TemplateView.as_view(template_name='cafe/cart.html'), name='cart'),
    url(r'^cart/render/$', views.RenderCartView.as_view(), name='render_cart')
]
