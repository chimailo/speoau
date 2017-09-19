from django.contrib import admin
from .models import Member

# Register your models here.

def add_one(modeladmin, request, queryset):
	for user in queryset:
		if user.level < 6:
			user.level += 1

			if user.level > 5:
				user.is_alumni = True
				user.level = 6
			
		user.save()
add_one.short_description = 'Increase level'

class MemberAdmin(admin.ModelAdmin):
	fieldsets = [
		('Info', {'fields': ['fullname','gender', 'dept', 'phone', 'email', 'level', 'committee']
		}),
	]

	list_display = ('__str__', 'phone', 'email', 'dept', 'level', 'gender', 'committee')
	list_filter = ['level', 'dept', 'committee']
	actions = [add_one,]
	search_fields = ['fullname', 'dept',]

admin.site.register(Member, MemberAdmin)
