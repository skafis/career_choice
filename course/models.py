from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Courses(models.Model):
	name = models.CharField(max_length=200)
	time = models.IntegerField()
	cost = models.IntegerField()

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name
        
class Course_instructor(models.Model):
	first_name = models.CharField(max_length=140)
	last_name = models.CharField(max_length= 140)
	specialty = models.CharField(max_length = 200)

	def __unicode__(self):
	    return self.specialty

	def __str__(self):
	    return self.specialty

class Learners(models.Model):
	first_name = models.CharField(max_length=140)
	last_name = models.CharField(max_length= 140)
	career_intrest = models.CharField(max_length=200)

	def __unicode__(self):
	    return self.career_intrest

	def __str__(self):
	    return self.career_intrest
