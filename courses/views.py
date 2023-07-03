from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def courses(request):
    return HttpResponse('Course List')

def details(request, course_name):
    return HttpResponse(f'{course_name} details')

def getCoursesByCategory(request, category_name):
    text= ''
    if(category_name=='coding'):
        text='coding courses'
    elif(category_name=='mobile-development'):
        text='Mobile Development Courses'
    else: text='There is no category under this name'
    return HttpResponse(text)

def getCoursesByCategoryId(request, category_id:int):
   text:int = category_id
   return HttpResponse(category_id)