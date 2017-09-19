from .models import Member
from django.shortcuts import render, redirect, get_object_or_404
import datetime
from .forms import RegistrationForm
from django.views.generic import View
# Create your views here.

def member_register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.alumni = False
			user.date = datetime.date.today()
			user.save()
			return redirect('home')
	else:
		form = RegistrationForm()
	return render(request, 'register/register.html', { 'form': form })

