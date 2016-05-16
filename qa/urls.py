from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/?$', views.login, name='login'),
    url(r'^signup/?$', views.signup, name='signup'),
    url(r'^question/(?P<id>\d+)/?$', views.question, name='question'),
    url(r'^ask/.*$', views.ask, name='ask'),
    url(r'^popular/?$', views.popular, name='popular'),
    url(r'^new/?$', views.new, name='new'),
]
