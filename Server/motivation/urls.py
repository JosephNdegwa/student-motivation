from django.conf import settings
from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.home_view,name='homeView'),
    path('staff-signup', views.staff_signup_view,name='staff-signup'),
    path('staff-login',views.staff_login_view,name='staff-login'),
    path('staff/',views.staffclick_view,name='staffclick'),
    path ('student/',views.studentclick_view,name='studentclick'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    #path('post',views.article,name='post'),
]
