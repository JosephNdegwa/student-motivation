from django import forms
from django.contrib.auth.models import User
from . import models





class StaffUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class StaffForm(forms.ModelForm):
    class Meta:
        model=models.Staff
        fields=['mobile']




class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class StudentForm(forms.ModelForm):
    assignedStaffId=forms.ModelChoiceField(queryset=models.Staff.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Student
        fields=['mobile']






