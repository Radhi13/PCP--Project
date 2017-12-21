from django.conf.urls import url, include
from django.views.generic import ListView, DetailView

from blog.models import Post  #dont need this
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='list'),
	url(r'^post/(?P<id>\d+)/$', views.post_detail, name='detail'),
	url(r'^post/(?P<id>\d+)/edit/$', views.post_update, name='update'),
	url(r'^(?P<id>\d+)/delete/$', views.post_delete, name='delete'),
	#url(r'^(?P<pk>\d+)$', DetailView.as_view(
	#	model = Post,
	#	template_name="blog/post_detail.html")),
	url(r'^create/$', views.post_create,name='post_create'),
	
	

            ]
