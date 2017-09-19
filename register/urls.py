from . import views
from django.conf.urls import url

app_name = 'register'

urlpatterns = [
		
		# /members/register/
		url(r'^register/$', views.member_register, name='register')
	]
