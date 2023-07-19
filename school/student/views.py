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
    return render(request,'courses.html',{'courses':courses,})
    
def teacher(request):
    teacher = AddTeacher.objects.all()
    return render(request,'teacher.html',{'teacher':teacher})
    
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
    
def addteachers(request):
    if request.method == 'POST':
        tname = request.POST['tname']
        temail = request.POST['temail']
        tmobile = request.POST['tmobile']
        taddress= request.POST['taddress']
        experience = request.POST['experience']
        salary = request.POST['salary']
        if AddTeacher.objects.filter(temail = temail).exists():
            messages.error(request,'email already exists')
            return redirect('/addteachers/')
        
        elif AddTeacher.objects.filter(tmobile = tmobile).exists():
            messages.error(request,'mobile no is already exists')
            return redirect('/addteachers/')
        else:
            AddTeacher.objects.create(tname = tname, 
                                       temail = temail,
                                       tmobile = tmobile,
                                       taddress = taddress,
                                       experience = experience,
                                       salary = salary,
                                       )
            messages.success(request,'student added successfully')
            teacher = AddTeacher.objects.all()
            return render(request, 'teacher.html', {'teacher': teacher})
    else:
        teacher = AddTeacher.objects.all()
        return render(request, 'teacher.html', {'teacher': teacher})


def deletecourse(request,pk):
    AddCourses.objects.get(id = pk).delete()
    return redirect('/courses/')

def deletestudent(request,pk):
    AddCourses.objects.get(id = pk).delete()
    return redirect('/viewstudents/')

def deleteteacher(request,pk):
    AddTeacher.objects.get(id = pk).delete()
    return redirect('/teacher/')

def updatecourse(request,uid):
    res = AddCourses.objects.get(id =uid)
    return render(request, 'updatecourse.html',context={'stu':res,})

def updatestudent(request,sid):
    res = AddStudents.objects.get(id =sid)
    addcourse = AddCourses.objects.all()
    return render(request, 'updatestudent.html',context={'stu':res,'addcourse':addcourse})

def updateteacher(request,tid):
    res = AddTeacher.objects.get(id = tid)
    return render(request, 'updateteacher.html',context={'teacher':res,})

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
    
def update_teacher_data(request):
    if request.method =='POST':
        tid = request.POST['tid']
        tname = request.POST['tname']
        temail = request.POST['temail']
        tmobile = request.POST['tmobile']
        taddress= request.POST['taddress']
        experience = request.POST['experience']
        salary = request.POST['salary']
        AddTeacher.objects.filter(id = tid).update(tname = tname, temail = temail, tmobile = tmobile, taddress = taddress, experience = experience, salary = salary)
        return redirect('/teacher/')

def search_student(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(sname__icontains = q) | Q(semail__icontains = q)) |Q(smobile__icontains = q)
        stu = AddStudents.objects.filter(multiple_q)
    else:
        stu = AddStudents.objects.all()
    context = {'stu':stu}
    return render(request,'viewstudents.html',context)

def search_course(request):
    if 'q' in request.GET:
        q = request.GET['q']
        courses = AddCourses.objects.filter(course__icontains = q)
    else:
        courses = AddCourses.objects.all()
    context = {'courses':courses}
    return render(request,'courses.html',context)

def search_teacher(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(tname__icontains = q) | Q(temail__icontains = q)) |Q(tmobile__icontains = q)
        teacher = AddTeacher.objects.filter(multiple_q)
    else:
        teacher = AddTeacher.objects.all()
    context = {'teacher':teacher}
    return render(request,'teacher.html',context)

