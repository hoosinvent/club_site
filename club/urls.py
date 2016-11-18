from django.conf.urls import url

from django.contrib.auth import views as auth_views



from . import views



urlpatterns = [
	url(r'adroit/$', views.adroit, name='adroit'),
	url(r'wheels/$', views.wheels, name='wheels'),
	url(r'laser/$', views.laser, name='laser'),
	url(r'sound/$', views.sound, name='sound'),
	url(r'project/$', views.project, name='project'),
	url(r'contact/$', views.contact, name='contact'),
	url(r'$', views.index, name='index'),
]
