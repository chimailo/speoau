from django.test import TestCase, client
from django.urls import reverse
from .models import Member
from .forms import RegistrationForm
from . import views

# models tests
class RegistrationModelTest(TestCase):
	""" Tests for the registration model """

	@classmethod
	def setUpTestData(cls):
		# Set up test data for the whole site
		cls.member = Member.objects.create(surname='Orlando', first_name='Julius', other_name='James',
							phone='08180323025', email='foobar@yahoo.com', matric_no='che/2013/051')

	def test_name_is_surname_firstname_and_maybe_othername(self):
		member = Member.objects.get(matric_no='che/2013/051')
		if member.other_name:
			exp_name_format = '%s %s %s' % (member.surname.upper(), member.first_name, member.other_name)
			self.assertEquals(exp_name_format, str(member))
		else:
			exp_name_format = '%s %s' % (member.surname.upper(), member.first_name)
			self.assertEquals(exp_name_format, str(member))

	def test_get_absolute_url(self):
		member = Member.objects.get(matric_no='che/2013/051')
		self.assertEquals(member.get_absolute_url(),
						reverse('registration:member_detail', args=(self.member.id,)))
	
	def test_email_field_label(self):
		self.member = Member.objects.get(matric_no='che/2013/051')
		field_label = self.member._meta.get_field('email').verbose_name
		self.assertEquals(field_label, 'Email Address')

	def test_matric_no_label(self):
		member = Member.objects.get(matric_no='che/2013/051')
		field_label = member._meta.get_field('matric_no').verbose_name
		self.assertEquals(field_label, 'Matric Number')

	def test_reg_date_label(self):
		member = Member.objects.get(matric_no='che/2013/051')
		field_label = member._meta.get_field('reg_date').verbose_name
		self.assertEquals(field_label, 'Date Registered')



# form Tests

class RegistrationFormTest(TestCase):
	""" Tests for the registration form """

	def test_matric_number_not_beyond_present_date(self):
		s = Member.objects.create(surname='Pemberton', first_name='Pious', other_name='Odion',
						phone='08186030925', email='foobar@gmail.com', matric_no='che/2017/051')
		data = {'surname':s.surname, 'first_name':s.first_name, 'other_name':s.other_name,
				'phone':s.phone, 'email':s.email, 'matric_no':s.matric_no,}
		form = RegistrationForm(data=data)
		self.assertFalse(form.is_valid())

	def test_matric_serial_number_not_above_150(self):
		s = Member.objects.create(surname='Pemberton', first_name='Pious', other_name='Odion',
						phone='08186030925', email='foobar@gmail.com', matric_no='che/2013/151')
		data = {'surname':s.surname, 'first_name':s.first_name, 'other_name':s.other_name,
				'phone':s.phone, 'email':s.email, 'matric_no':s.matric_no,}
		form = RegistrationForm(data=data)
		self.assertFalse(form.is_valid())

	def test_phone_no_not_less_than_11_digits(self):
		s = Member.objects.create(surname='Pemberton', first_name='Pious', other_name='Odion',
						phone='0818600925', email='foobar@gmail.com', matric_no='che/2013/051')
		data = {'surname':s.surname, 'first_name':s.first_name, 'other_name':s.other_name,
				'phone':s.phone, 'email':s.email, 'matric_no':s.matric_no,}
		form = RegistrationForm(data=data)
		self.assertFalse(form.is_valid())

	def test_email_provider_is_yahoo_or_gmail(self):
		s = Member.objects.create(surname='Pemberton', first_name='Pious', other_name='Odion',
						phone='08186020925', email='foobar@stuff.com', matric_no='che/2013/051')
		data = {'surname':s.surname, 'first_name':s.first_name, 'other_name':s.other_name,
				'phone':s.phone, 'email':s.email, 'matric_no':s.matric_no,}
		form = RegistrationForm(data=data)
		self.assertFalse(form.is_valid())


# views tests

class RegistrationViewsTests(TestCase):
	""" Tests for the Registraton Views """

	@classmethod
	def setUpTestData(cls):
		# Set up test data for the whole site
		cls.member = Member.objects.create(surname='Orlando', first_name='Julius', other_name='James', gender='M',
									phone='08180323025', email='foobar@yahoo.com', matric_no='che/2013/051')


	def test_member_detail_view_available_at_specified_url(self):
		response = self.client.get(reverse('registration:member_detail', args=(self.member.id,)))
		self.assertEqual(response.status_code, 200)

	def test_member_detail_view_context_data(self):
		response = self.client.get(reverse('registration:member_detail', args=(self.member.id,)))
		self.assertEqual(response.context['member'], self.member)

	def test_member_detail_view_served_response(self):
		response = self.client.get(reverse('registration:member_detail', args=(self.member.id,)))
		self.assertEqual(response.resolver_match.func, views.member_detail)

	def test_member_detail_view_template(self):
		response = self.client.get(reverse('registration:member_detail', args=(self.member.id,)))
		self.assertTemplateUsed(response, 'registration/detail.html')

	def test_register_success_view_available_at_specified_url(self):
		response = self.client.get(reverse('registration:register_success'))
		self.assertEqual(response.status_code, 200)

	def test_member_register_success_view_template(self):
		response = self.client.get(reverse('registration:register_success'))
		self.assertTemplateUsed(response, 'registration/register_success.html')

	def test_member_register_view_is_displayed_at_desired_url(self):
		response = self.client.get(reverse('registration:member_register'))
		self.assertEqual(response.status_code, 200)

	def test_member_register_view_template_and_context_used(self):
		response = self.client.get(reverse('registration:member_register'))
		self.assertTemplateUsed(response, 'registration/memberform.html')
		#self.assertIn(response.context, 'form')

	def test_member_edit_view_is_displayed_at_desired_url(self):
		response = self.client.get(reverse('registration:member_update', args=(self.member.id,)))
		self.assertEqual(response.status_code, 200)

	def test_member_edit_view_template_and_context_used(self):
		response = self.client.get(reverse('registration:member_update', args=(self.member.id,)))
		self.assertTemplateUsed(response, 'registration/memberform.html')
		#self.assertIn(response.context, 'form')