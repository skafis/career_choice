from django import forms
from .models import Courses

class add_coursesForm(forms.ModelForm):
	class Meta:
		model = Courses
		fields = [
		'name',
		'time',
		'cost'
		]