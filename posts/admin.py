from django.contrib import admin
from posts.models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
	fieldsets = [
		('Create Event', {'fields': ['event', 'summary', 'event_desc',]}),
		('Date information', {'fields': ['event_date']}),
	]


	list_display = ('__str__', 'summary', 'event_date', 'post_date')
	search_fields = ['event', 'summary']


admin.site.register(Event, EventAdmin)


