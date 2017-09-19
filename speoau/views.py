from django.shortcuts import render
from register.models import Member
from posts.models import Event
from datetime import date
from django.contrib.auth.models import User


def home(request):
	user = User.objects.all()
	event_all = Event.objects.filter(post_date__isnull=False)
	events = event_all.filter(event_date__gte=date.today()).order_by('event_date')[:4]
	return render(request, 'home.html', {'events':events, 'user':user})
