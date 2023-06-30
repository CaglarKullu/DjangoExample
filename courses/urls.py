
from django.urls import path


from courses.views import courses, home


urlpatterns = [
    path('', home),
    path('home', home),
    path('course_list',courses),
]
