from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'sign-up.html')

def dashboard(request):
    return render(request,'dashboard.html')

def courses(request):
    courses = AddCourses.objects.filter(is_active=True).order_by('id')
    return render(request,'courses.html',{'request':request,'courses':courses})

def employees(request):
    return render(request,'employees.html')

def hostel(request):
    return render(request,'hostel_details.html')

def notifications(request):
    return render(request,'notifications.html')

def pg_dashboard(request):
    return render(request,'pg_dashboard.html')
    
def profile(request):
    return render(request,'profile.html')
    
def tables(request):
    return render(request,'tables.html')
    
def tenants(request):
    return render(request,'tenants.html')
    
def viewstudents(request):
    stu = AddStudents.objects.all()
    addcourse = AddCourses.objects.all()
    return render(request,'viewstudents.html',{'stu':stu,
    'addcourse':addcourse})


def form_data(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if Registration.objects.filter(email = email).exists():
            messages.error(request,'email already exists')
            return redirect('/signup/')
        else:
            Registration.objects.create(name = name,email = email, password = password)
            messages.success(request,'registration successful')
            return redirect('/')
        
def login(request):
    if request.method =='POST':
        username = request.POST['email']
        user_password = request.POST['password']
        if Registration.objects.filter(email = username).exists():
            obj = Registration.objects.get(email = username)
            password = obj.password
            if check_password(user_password,password):
                return redirect('/dashboard/')
            else:
                messages.error(request,'password is incorrect')
                return redirect('/')
        else:
            messages.error(request,'email is not registered')
            return redirect('/')      

def addcourses(request):
    if request.method == 'POST':
        c_name = request.POST['CourseName']
        c_fees = request.POST['CourseFees']
        c_duration = request.POST['Duration']
        c_desc = request.POST['CourseDesc']
        messages.success(request,'Course Added Successfully')
        AddCourses.objects.create(course = c_name, fees = c_fees, duration = c_duration, desc =c_desc)
        return redirect('/courses/')
    
def deletecourse(request,pk):
    AddCourses.objects.get(id = pk).delete()
    return redirect('/courses/')

def deletestudent(request,pk):
    AddCourses.objects.get(id = pk).delete()
    return redirect('/viewstudents/')

def updatecourse(request,uid):
    res = AddCourses.objects.get(id =uid)
    return render(request, 'updatecourse.html',context={'stu':res,})

def updatestudent(request,sid):
    res = AddStudents.objects.get(id =sid)
    addcourse = AddCourses.objects.all()
    return render(request, 'updatestudent.html',context={'stu':res,'addcourse':addcourse})

def update_crs_data(request):
    if request.method =='POST':
        uid = request.POST['uid']
        c_name = request.POST['CourseName']
        c_fees = request.POST['CourseFees']
        c_duration = request.POST['Duration']
        c_desc = request.POST['CourseDesc']
        AddCourses.objects.filter(id = uid).update(course = c_name, fees = c_fees, duration = c_duration, desc = c_desc)
        return redirect('/courses/')
    
def update_stu_data(request):
    if request.method =='POST':
        sid = request.POST['sid']
        stu_name = request.POST['Name']
        stu_email = request.POST['Email']
        stu_mobile = request.POST['Mobile']
        stu_college = request.POST['College']
        stu_degree = request.POST['Degree']
        stu_addcourse_id = request.POST.get('course')
        stu_address = request.POST['Address']
        stu_course = AddCourses.objects.get(id = stu_addcourse_id)
        AddStudents.objects.filter(id = sid).update(sname = stu_name, semail = stu_email, smobile = stu_mobile, scollege = stu_college, sdegree = stu_degree, saddress = stu_address, scourses = stu_course)
        return redirect('/viewstudents/')
    
def addstudents(request):
    if request.method == 'POST':
        stu_name = request.POST.get('Name')
        stu_email = request.POST.get('Email')
        stu_mobile = request.POST.get('Mobile')
        stu_college = request.POST.get('College')
        stu_degree = request.POST.get('Degree')
        stu_addcourse_id = request.POST.get('course')
        stu_address = request.POST.get('Address')
        stu_course = AddCourses.objects.get(id = stu_addcourse_id)
        if AddStudents.objects.filter(semail = stu_email).exists():
            messages.error(request,'email already exists')
            return redirect('/addstudents/')
        
        elif AddStudents.objects.filter(smobile = stu_mobile).exists():
            messages.error(request,'mobile no is already exists')
            return redirect('/addstudents/')
        else:
            AddStudents.objects.create(sname = stu_name, 
                                       semail = stu_email,
                                       smobile = stu_mobile,
                                       scollege = stu_college,
                                       scourses = stu_course,
                                       sdegree = stu_degree,
                                       saddress = stu_address,
                                       )
            messages.success(request,'student added successfully')
            stu = AddStudents.objects.all()
            addcourse =AddCourses.objects.all()
            return render(request, 'viewstudents.html', {'stu': stu,'addcourse':addcourse})
    else:
        stu = AddStudents.objects.all()
        addcourse =AddCourses.objects.all()
        return render(request, 'viewstudents.html', {'stu': stu,'addcourse':addcourse})


def searchstu(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(sname__icontains = q) | Q(semail__icontains = q)) |Q(smobile__icontains = q)
        stu = AddStudents.objects.filter(multiple_q)
    else:
        stu = AddStudents.objects.all()
    context = {'stu':stu}
    return render(request,'viewstudents.html',context)
