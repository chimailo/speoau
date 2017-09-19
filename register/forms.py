from django import forms
from .models import Member
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ['fullname', 'level', 'phone','gender', 'email', 'dept']

		widgets = {'fullname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fullname', 'id':'fullname'}),
		          'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number', 'id':'phone'}),
		          'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email', 'id':'email'}),
		          'dept': forms.Select(attrs={'class':'form-control', 'placeholder':'Select Your Department'}),
		          'gender': forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}),
		          'level': forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}),
        }


	def clean_email(self):
		email = self.cleaned_data['email']
		sth, prov = email.split("@")
		ext = ['yahoo.com', 'gmail.com']
		if (prov not in ext):
			raise forms.ValidationError('Please enter a gmail or yahoo mail address')
		return email
