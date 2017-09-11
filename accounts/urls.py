from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


app_name = 'accounts'


urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    url(r'profile/$', views.profile, name='profile'),
    url(r'^statistics/$', views.statistics, name='statistics'),
    url(r'^order/$', views.order, name='order'),
    # url(r'^order/(?P<token>.+)/$', views.order, name='order'),
    url(r'^set_order_status/$', views.set_order_status, name='set_order_status'),
]
