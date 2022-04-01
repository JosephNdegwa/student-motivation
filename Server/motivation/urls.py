from django.conf import settings
from django.urls import path,include
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views
from .views import(
    AuthUserRegistrationView,AuthUserLoginView,
    AuthLogoutView,UserListView,
)
urlpatterns=[
    path('post/', views.post), 
    #path('',views.home_view,name='homeView'),
    #path('staff/',views.staffclick_view, name="staffclick"),
    #path('staff-signup', views.staff_signup_view,name='staff-signup'),
    #path('staff-login',views.staff_login_view,name='staff-login'),
    #path('staff/',views.staffclick_view,name='staffclick'),
    #path ('student/',views.studentclick_view,name='studentclick'),
    #path('afterlogin', views.afterlogin_view,name='afterlogin'),
    #path('post',views.article,name='post'),
]
