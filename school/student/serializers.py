from rest_framework import serializers
from . models import *

class AddStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddStudents
        fields = '__all__'

class AddCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCourses
        fields = '__all__'

class AddTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddTeacher
        fields = '__all__'