from django.conf.urls import patterns, url

from hotspot import views

urlpatterns = patterns('',
	url(r'^$', views.HomePageView.as_view(), name='hotspot.index'),
	url(r'^help$', views.HelpPageView.as_view(), name='hotspot.help'),
	url(r'^redirect$', views.redirectLogin, name='hotspot.redirect'),
)
