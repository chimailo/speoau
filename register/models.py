from django.db import models
import datetime
from django.core.urlresolvers import reverse

# Create your models here.

class Member(models.Model):

	LEVEL = (
		(1, 100),
		(2, 200),
		(3, 300),
		(4, 400),
		(5, 500),
		(6, 600),
		)
	
	GENDER = (
		('F', 'female'),
		('M', 'male')
		)

	DEPT = (
		('age', 'Agricultural Engineering'),
		('bch', 'Biochemistry'),		
		('che', 'Chemical Engineering'),
		('chm', 'Chemistry'),
		('cve', 'Civil Engineering'),
		('csc', 'Computer Engineering'),
		('eee', 'Elect. Elect. Engineering'),
		('geo', 'Geology'),
		('msc', 'Materials Science Engineering'),
		('mth', 'Mathematics'),
		('mee', 'Mechanical Engineering'),
		('phy', 'Physics'),
		)

	COMMITTEES = (
		('cty', 'Catch Them Young'),
		('com', 'Petro Bowl / Quiz'),
		('reg', 'Registration'),
	)


	fullname = models.CharField(max_length=30, default='')
	phone = models.CharField(max_length=11, blank=True)
	gender = models.CharField('sex', max_length=1, choices=GENDER)
	email = models.EmailField(max_length=30, unique=True)
	level = models.IntegerField(choices=LEVEL)
	dept = models.CharField('Department', max_length=3, choices=DEPT)
	reg_date = models.DateField('Date Registered', auto_now_add=True)
	alumni = models.BooleanField(default=False)
	committee = models.CharField(max_length=3, default='', choices=COMMITTEES)


	def __str__(self):
		"""Returns the fullname."""
		return self.fullname.strip()

	def get_short_name(self):
		"""Returns the short name for the user."""
		return self.first_name

	def get_absolute_url(self):
		return reverse('register:member_detail', kwargs={'pk':self.pk})
