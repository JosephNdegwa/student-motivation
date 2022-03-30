from multiprocessing import context
from django.shortcuts import render
from motivation.models import Staff
# Create your views here.

def Staff(request,name):
    staff = Staff.objects.get(name=name)
    context = {'staff':staff}
    return render(request,'staff.html')