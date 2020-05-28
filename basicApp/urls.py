from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from basicApp import views


app_name = "basicApp"

urlpatterns = [
	url(r'^$' , views.index1, name = "index"),
	url(r'^index/', views.index , name = "index"),
	url(r'^other/', views.other , name = "other"),
	url(r'^register/', views.register , name = "register"),
	url(r'^login/' , views.user_login , name = "login"),
	url(r'^logout/', views.user_logout , name = "logout"),
	url(r'^relative_url_templates/', views.relative_url_templates , name = "relative_url_templates"),
]