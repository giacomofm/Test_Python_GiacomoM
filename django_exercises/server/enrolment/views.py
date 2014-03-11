from django.shortcuts import render
from enrolment.models import student
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def school_day(request):
    if request.method == 'POST':
        body = request.body
        content = json.loads(body)
        all_student = student(first_name=content['first_name'],last_name=content['last_name'])
        all_student.save()
        return HttpResponse(status=200)
    elif request.method == 'GET':
        all_student = student.objects.all()
        list_student = [{'first_name':list_temp_stud.first_name,'last_name':list_temp_stud.last_name}for list_temp_stud in all_student]
        resp = json.dumps(list_student)
        return HttpResponse(resp, content_type='application/json')