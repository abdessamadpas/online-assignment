from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from core.models import *
from django.template import loader
from django.http import HttpResponse

def dashboard(request):
    models_total = Matiere.objects.all().count()
    exams_total = Exam.objects.all().count()
    students_total = Student.objects.all().count()
    template = loader.get_template('admine/pages/index.html')
    context = {
        'models_total': models_total,
        'exams_total': exams_total,
        'students_total': students_total,
    }

    return HttpResponse(template.render(context, request))