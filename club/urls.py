from django.conf.urls import url

from django.contrib.auth import views as auth_views



from . import views



urlpatterns = [
	url(r'project/$', views.project, name='project'),
	url(r'contact/$', views.contact, name='contact'),
	url(r'$', views.index, name='index'),
]
