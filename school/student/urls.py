from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('courses/', views.courses, name='courses'),
    path('viewstudents/', views.viewstudents, name='viewstudents'),
    path('registration/', views.form_data, name='registration'),
    path('login/', views.login, name='login'),
    path('teacher/', views.teacher, name='teacher'),
    path('addcourses/', views.addcourses, name='addcourses'),
    path('addteachers/', views.addteachers, name='addteachers'),
    path('addstudents/', views.addstudents, name='addstudents'),
    path('deletecourse/<pk>/',views.deletecourse,name='deletecourse'),
    path('deletestudent/<pk>/',views.deletestudent,name='deletestudent'),
    path('deleteteacher/<pk>/',views.deleteteacher,name='deleteteacher'),
    path('updatecourse/<int:uid>/',views.updatecourse,name='updatecourse'),
    path('updatestudent/<int:sid>/',views.updatestudent,name='updatestudent'),
    path('updateteacher/<int:tid>/',views.updateteacher,name='updateteacher'),
    path('update_crs_data/',views.update_crs_data,name='update_crs_data'),
    path('update_stu_data/',views.update_stu_data,name='update_stu_data'),
    path('update_teacher_data/',views.update_teacher_data,name='update_teacher_data'),
    path('search_student/',views.search_student,name='search_student'),
    path('search_course/',views.search_course,name='search_course'),
    path('search_teacher/',views.search_teacher,name='search_teacher'),
]