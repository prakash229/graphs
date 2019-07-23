from django.conf.urls import include, url
from . import views

urlpatterns =[
	url(r'^$', views.index, name='index'),
    url(r'^$', views.preview, name='preview'),
    url(r'^login', views.login, name = 'hello'),
    url(r'^plot', views.test_matplotlib, name = 'plot'),
    url(r'^hist', views.matplot, name = 'hist'),
    url(r'^hgram', views.hgram, name = 'user'),
]


