from django.shortcuts import render
from django.conf import settings
from . import forms,models
from django.contrib.auth.models import Group

from django.http import HttpResponseRedirect


# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'index.html')



#for showing signup/login button for staff
def staffclick_view(request):
    if request.user.is_authenticated:
        # return HttpResponseRedirect('afterlogin')
        return render(request,'staffclick.html')


#for showing signup/login button for student
def studentclick_view(request):
    if request.user.is_authenticated:
        # return HttpResponseRedirect('afterlogin')
       return render(request,'motiversity/studentclick.html')



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
        return HttpResponseRedirect('stafflogin')
    return render(request,'staff-signup.html',context=mydict)



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



