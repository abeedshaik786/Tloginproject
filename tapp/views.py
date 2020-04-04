from django.shortcuts import render,redirect
from .forms import addForm
from .forms import StudentRegisterForm,TeacherRegisterForm
from .models import User,add
from django.contrib.auth import get_user_model
from django.views.generic import CreateView,FormView
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,get_user_model
from django.http import HttpResponse
from django.utils.http import is_safe_url
from django.contrib import messages
from .decorators import student_required,teacher_required
from django.contrib.auth.decorators import login_required
# Create your views here.
def home (request):
    return render(request, 'tapp/home.html')

def logout(request):
    logout(request)
    return redirect('/')


def python (request):
    return render(request, 'tapp/python.html')

#@teacher_required
def java (request):
    return render(request, 'tapp/java.html')

#@student_required
def c(request):
    return render(request, 'tapp/c.html')

@login_required
def add_student(request):
    return render(request, 'tapp/add Student.html')

@login_required
def add_teacher(request):
    return render(request, 'tapp/add Teacher.html')

User = get_user_model()
def teacher_reg(request):
    form=TeacherRegisterForm()
    if request.method =='POST':
        form=TeacherRegisterForm(request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            email=request.POST.get('email')
            branch=request.POST.get('branch')
            gender=request.POST.get('gender')
            phone=request.POST.get('phone')
            password=request.POST.get('password')
            if User.objects.filter(username=username).exists():
                messages.info(request,'!That username is already taken.')
                return redirect('teacher_reg.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'!That email is already taken.')
                return redirect('teacher_reg.html')
            elif User.objects.filter(phone=phone).exists():
                messages.info(request,'!That phone is already taken.')
                return redirect('teacher_reg.html')
            else:
                form.save()
                print('form was successfully submited')

        else:
            messages.info(request,'!Enter valid Credensionials')
            return redirect('teacher_reg.html')
        return redirect('teacher_log.html')
    else:
        return render(request,'tapp/teacher_reg.html',{'form':form})

def teacher_log(request):
    if request.method =='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        UserModel = get_user_model()
        user=auth.authenticate(email=email,password=password)
        validation = User.objects.get(email=email)
        if validation.is_staff == True:
            if user is not None:
                auth.login(request,user)
                user_data = User.objects.get(email=email)
                return render(request,'tapp/java.html')
        else:
            messages.info(request,'! Invalid User id/Password')
            return redirect('teacher_log.html')
    else:
        return render(request,'tapp/teacher_log.html')

def student_log(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=auth.authenticate(email=email,password=password)
        User = get_user_model()
        validation = User.objects.get(email=email)
        if validation.is_staff == False:
            if user is not None:
                auth.login(request,user)
                user_data = User.objects.get(email=email)
                return render(request,"tapp/c.html")
        else:
            messages.info(request,'!Your credentials are invalid. Please try again.')
            return redirect('student_log.html')
    else:
        return render(request,'tapp/student_log.html')


User = get_user_model()
def student_reg(request):
    form=StudentRegisterForm()
    if request.method =='POST':
        form=StudentRegisterForm(request.POST)
        if form.is_valid() :
            username=request.POST.get('username')
            email=request.POST.get('email')
            rollnumber=request.POST.get('rollnumber')
            branch=request.POST.get('branch')
            year=request.POST.get('year')
            phone=request.POST.get('phone')
            section=request.POST.get('section')
            backlogs=request.POST.get('backlogs')
            resume=resume.POST.get('resume')
            gender=request.POST.get('gender')
            password=request.POST.get('password')
            if User.objects.filter(rollnumber=rollnumber).exists():
                messages.info(request,'!That rollnumber is already taken.' )
                return redirect('student_reg.html')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'!That studentname is already taken.')
                return redirect('student_reg.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'!That email is already taken.')
                return redirect('student_reg.html')
            elif User.objects.filter(phone=phone).exists():
                messages.info(request,'!That phone is already taken.')
                return redirect('student_reg.html')
            else:
                form.save()
                print('form was successfully submited')
        else:
            messages.info(request,'!Enter valid Credensionials')
            return redirect('student_reg.html')
        return redirect('student_log.html')
    else:
        return render(request,'tapp/student_reg.html',{'form':form})


def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'!That username is already taken.' )
                return redirect('register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'!That Email is already taken.')
                return redirect('register.html')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
        else:
            messages.info(request,'! Password not matching')
            return redirect('register.html')
        return redirect('/')
    else:
        return render(request,'tapp/register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        User = get_user_model()
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'! Invalid User id/Password')
            return redirect('login.html')
    else:
        return render(request,'tapp/login.html')


def genarate(request):
    qs = add.objects.all()
    subject=request.GET.get('subject')
    branch=request.GET.get('branch')
    deficulty=request.GET.get('deficulty')
    question=request.GET.get('question')
    if is_valid_queryparam(subject):
        qs = qs.filter(subject=subject)
    if is_valid_queryparam(branch):
        qs = qs.filter(branch=branch)
    if is_valid_queryparam(deficulty):
        qs = qs.filter(deficulty=deficulty)
    if is_valid_queryparam(question):
        qs = qs.filter(question=question)
    return render(request,'tapp/Genarate question Paper.html')

def add_questions(request):
    form=addForm()
    if request.method =='POST':
        form=addForm(request.POST)
        if form.is_valid():
            subject=request.GET.get('subject')
            deficulty=request.GET.get('deficulty')
            question=request.GET.get('question')
            Option1=request.GET.get('Option1')
            Option2=request.GET.get('Option2')
            Option3=request.GET.get('Option3')
            Option4=request.GET.get('Option4')
            option=request.GET.get('option')
            add.subject=subject
            add.deficulty=deficulty
            add.question=question
            add.Option1=Option1
            add.Option2=Option2
            add.Option3=Option3
            add.Option4=Option4
            add.option=option
            form.save()

    return render(request,'tapp/add questions.html',{'form':form})
