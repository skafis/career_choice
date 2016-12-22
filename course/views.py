from django.shortcuts import render
from .models import Course_instructor, Courses, Learners
from .forms import add_coursesForm

# Create your views here.
def course_list(request):
	queryset = Courses.objects.all()
	ctx = {
		'queryset':queryset
	}
	return render(request, 'index.html', ctx)

def add_course(request):
	forms = add_coursesForm(request.POST or None)
	ctx = {}
	ctx['forms'] = forms
	if request.method == 'POST':
		if forms.is_valid():
			instance = form.save()
			return redirect('course_list')
	return render(request, 'add_course.html', ctx)