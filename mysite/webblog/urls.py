from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^feedback/', views.feedback_form, name='feedback'),
   ]
