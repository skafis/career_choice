from django.shortcuts import render
from .models import Course_instructor, Courses, Learners

# Create your views here.
def course_list(request):
	queryset = Courses.objects.all()

	context = {
		'queryset':queryset
	}
	return render(request, 'index.html', context)
