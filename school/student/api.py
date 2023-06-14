from rest_framework import generics
from rest_framework.response import Response
from . models import *
from . serializers import *

# class for addcourses api

class AddCoursesGetDataAPI(generics.ListAPIView):
    queryset = AddCourses.objects.all()
    serializer_class = AddCoursesSerializer

class AddCoursesGetOneDataAPI(generics.RetrieveAPIView):
    queryset = AddCourses.objects.all()
    serializer_class = AddCoursesSerializer

class AddCoursesCreateAPI(generics.CreateAPIView):
    queryset = AddCourses.objects.all()
    serializer_class = AddCoursesSerializer

class AddCoursesUpdateAPI(generics.UpdateAPIView):
    queryset = AddCourses.objects.all()
    serializer_class = AddCoursesSerializer

class AddCoursesUpdatePartialAPI(generics.RetrieveUpdateAPIView):
    queryset = AddCourses.objects.all()
    serializer_class = AddCoursesSerializer

class AddCoursesDeleteAPI(generics.DestroyAPIView):
    queryset = AddCourses.objects.all()
    serializer_class = AddCoursesSerializer

# class for addstudents api

class AddStudentsCreateAPI(generics.CreateAPIView):
    queryset = AddStudents.objects.all()
    serializer_class = AddStudentsSerializer

class AddStudentsGetONEDataAPI(generics.RetrieveAPIView):
    queryset = AddStudents.objects.all()
    serializer_class = AddStudentsSerializer

class AddStudentsGetDataAPI(generics.ListAPIView):
    queryset = AddStudents.objects.all()
    serializer_class = AddStudentsSerializer

class AddStudentsUpdateAPI(generics.UpdateAPIView):
    queryset = AddStudents.objects.all()
    serializer_class = AddStudentsSerializer

class AddStudentsUpdatePartialAPI(generics.RetrieveUpdateAPIView):
    queryset = AddStudents.objects.all()
    serializer_class = AddStudentsSerializer

class AddStudentsDeleteAPI(generics.DestroyAPIView):
    queryset = AddStudents.objects.all()
    serializer_class = AddStudentsSerializer

# class for addteacher api

class AddTeacherCreateAPI(generics.CreateAPIView):
    queryset = AddTeacher.objects.all()
    serializer_class = AddTeacherSerializer

class AddTeacherGetDataAPI(generics.ListAPIView):
    queryset = AddTeacher.objects.all()
    serializer_class = AddTeacherSerializer

class AddTeacherGetOneDataAPI(generics.RetrieveAPIView):
    queryset = AddTeacher.objects.all()
    serializer_class = AddTeacherSerializer

class AddTeacherUpdateAPI(generics.UpdateAPIView):
    queryset = AddTeacher.objects.all()
    serializer_class = AddTeacherSerializer

class AddTeacherUpdatePartialAPI(generics.RetrieveUpdateAPIView):
    queryset = AddTeacher.objects.all()
    serializer_class = AddTeacherSerializer

class AddTeacherDeleteAPI(generics.DestroyAPIView):
    queryset = AddTeacher.objects.all()
    serializer_class = AddTeacherSerializer