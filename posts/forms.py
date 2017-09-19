# from django import forms
# from .models import Event
# from tinymce.widgets import TinyMCE

# class EventForm(forms.ModelForm):

# 	event_desc = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

# 	widgets = {'event': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Event', 'id':'event'}),
# 		        'summary': forms.TextInput(attrs={'class':'form-control', 'placeholder':'A breif about the event in at most 30 words', 'id':'summary'}),
# 		        'event_date': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Date of the Event', 'id':'event_date'}),
# 		        'event_desc': forms.Select(attrs={'class':'form-control',})
#         }

# 	class Meta:
# 		model = Event
# 		fields = ['event', 'event_date', 'summary', 'event_desc']

