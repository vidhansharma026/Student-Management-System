from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pg_dashboard/', views.pg_dashboard, name='pg_dashboard'),
    path('courses/', views.courses, name='courses'),
    path('employees/', views.employees, name='employees'),
    path('hostel/', views.hostel, name='hostel'),
    path('notifications/', views.notifications, name='notifications'),
    path('profile/', views.profile, name='profile'),
    path('tables/', views.tables, name='tables'),
    path('tenants/', views.tenants, name='tenants'),
    path('viewstudents/', views.viewstudents, name='viewstudents'),
    path('registration/', views.form_data, name='registration'),
    path('login/', views.login, name='login'),
    path('addcourses/', views.addcourses, name='addcourses'),
    path('addstudents/', views.addstudents, name='addstudents'),
    path('deletecourse/<pk>/',views.deletecourse,name='deletecourse'),
    path('deletestudent/<pk>/',views.deletestudent,name='deletestudent'),
    path('updatecourse/<int:uid>/',views.updatecourse,name='updatecourse'),
    path('updatestudent/<int:sid>/',views.updatestudent,name='updatestudent'),
    path('update_crs_data/',views.update_crs_data,name='update_crs_data'),
    path('update_stu_data/',views.update_stu_data,name='update_stu_data'),
    path('searchstu/',views.searchstu,name='searchstu'),
]