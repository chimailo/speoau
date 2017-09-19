from .models import Event
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from django.conf import settings
import datetime
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.


class EventList(ListView):
	model = Event
	context_object_name = 'events'
	template_name = 'posts/events_list.html'

	def get_queryset(self):
		events = Event.objects.filter(post_date__isnull=False)
		return events.filter(event_date__gte=datetime.date.today()).order_by('event_date')


class EventDetail(DetailView):
	model = Event
	context_object_name = 'event'
	template_name = 'posts/event_detail.html'


def draft_list(request):
    events = Event.objects.filter(post_date__isnull=True).order_by('date_created')
    return render(request, 'posts/events_list.html', {'events': events})


@permission_required('event.add_event', login_url='/login')
def publish_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.publish()
    return redirect('event:all_events')


class DeleteEvent(PermissionRequiredMixin, DeleteView):
	model = Event
	success_url = reverse_lazy('event:draft_list')
	permission_required = 'event.delete_event'
	login_url='settings.LOGIN_URL'