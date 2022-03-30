from django.conf import settings
from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.home_view,name='homeView'),
    path('staff/',views.staffclick_view, name="staffclick"),
    path('staff-signup', views.staff_signup_view,name='staff-signup'),
    #path('post',views.article,name='post'),
]
