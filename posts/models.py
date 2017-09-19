from __future__ import unicode_literals
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
from django.core.urlresolvers import reverse
# Create your models here.


class Event(models.Model):
	event = models.CharField('title', max_length=100)
	event_date = models.DateField('date of event')
	summary = models.CharField(max_length=150, default='')
	event_desc = RichTextUploadingField('content')
	date_created = models.DateField(auto_now_add=True)
	post_date = models.DateField('date posted', blank=True, null=True)

	
	def __str__(self):
		return self.event

	def publish(self):
	    self.post_date = datetime.date.today()
	    self.save()

	def get_absolute_url(self):
		return reverse('posts:post_detail', kwargs={'pk':self.pk})
