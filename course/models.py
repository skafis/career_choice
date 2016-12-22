from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Courses(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	time = models.IntegerField()
	cost = models.IntegerField()

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def create_slug(instance,new_slug = None):
		slug = slugify(instance.name)
		if new_slug is not None:
			slug = new_slug
		qs = Courses.objects.filter(slug=slug).order_by("-id")
		exists = qs.exists()

		if exists:
			new_slug = "%s-%s" %(slug, qs.first().id)
			return create_slug(instance, new_slug=new_slug)
		return slug

	def pre_save_receiver(sender, instance, *args, **kwargs): 
	    if not instance.slug:
	        instance.slug = create_slug(instance)
        
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
