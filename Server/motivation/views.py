from django.shortcuts import render,redirect,reverse
from django.conf import settings
from . import forms,models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required



# Create your views here.
def home_view(request):
    # if request.user.is_authenticated:
     return render(request,'index.html')








#for showing signup/login button for staff
def staffclick_view(request):
    if request.user.is_authenticated:
        #return HttpResponseRedirect('afterlogin')
        return render(request,'staffclick.html')


#for showing signup/login button for student
def studentclick_view(request):
    if request.user.is_authenticated:
        #return HttpResponseRedirect('afterlogin')
        return render(request,'studentclick.html')



def staff_signup_view(request):
    userForm=forms.StaffUserForm()
    staffForm=forms.StaffForm()
    mydict={'userForm':userForm,'staffForm':staffForm}
    if request.method=='POST':
        userForm=forms.StaffUserForm(request.POST)
        staffForm=forms.StaffForm(request.POST,request.FILES)
        if userForm.is_valid() and staffForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            staff=staffForm.save(commit=False)
            staff.user=user
            staff=staff.save()
            my_staff_group = Group.objects.get_or_create(name='STAFF')
            my_staff_group[0].user_set.add(user)
        return HttpResponseRedirect('staff-login')
    return render(request,'staff-signup.html',context=mydict)

@login_required
def staff_login_view(request):
    return render(request,'staff-login.html')


def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.PatientForm()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student=student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request,'studentsignup.html',context=mydict)







def Post(request, title):
    post = Post.objects.get(title = title)
    context = {'post':post}
    return render(request,'post.html')


def is_staff(user):
    return user.groups.filter(name='STAFF').exists()


# Check if credential match8
def afterlogin_view(request):
    if is_staff(request.user):
        accountapproval=models.Staff.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('index.html')
        else:
            return render(request,'index.html')




