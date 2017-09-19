from . import views
from django.conf.urls import url

app_name = 'posts'

urlpatterns = [
		url(r'^all/$', views.EventList.as_view(), name='all_event'),
		url(r'^(?P<pk>\d+)/$', views.EventDetail.as_view(), name='event_detail'),
		url(r'^del/(?P<pk>\d+)/$', views.DeleteEvent.as_view(), name='event_delete'),
		url(r'^drafts/$', views.draft_list, name='draft_list'),
		url(r'^article/(?P<pk>\d+)/publish/$', views.publish_event, name='publish_event'),
]