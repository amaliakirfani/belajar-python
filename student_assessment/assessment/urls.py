from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    #path('', views.index),
    path('students/', views.show_students),
    path('students/edit/<id>', views.edit_data),
    path('students/delete/<id>', views.delete_student),

    path('lecturer/', views.show_lecturer),
    path('lecturer/edit/<id>', views.edit_data),
    path('lecturer/delete/<id>', views.delete_lecturer),

    path('courses/', views.show_courses),
    path('courses/edit/<id>', views.edit_data),
    path('courses/delete/<id>', views.delete_courses),

    path('grade/', views.show_grade),
    path('grade/edit/<id>', views.edit_data),
    path('grade/delete/<id>', views.delete_grade)
]