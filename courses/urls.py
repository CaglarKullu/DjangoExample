
from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses),
    path('list',views.courses),
    path('<course_name>',views.details),
    path('cagetories/category<int:category_id>',views.getCoursesByCategoryId),
    path('cagetories/<str:category_name>',views.getCoursesByCategory),

 
]
