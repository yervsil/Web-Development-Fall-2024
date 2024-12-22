from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Course
from django.template import loader

# Create your views here.
class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        template = loader.get_template('courses.html')
        context = {'courses': courses}
        return HttpResponse(template.render(context, request))

class CourseDetailView(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        template = loader.get_template('course_detail.html')
        context = {'course': course}
        return HttpResponse(template.render(context, request))