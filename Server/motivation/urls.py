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
    path('post/mot-id/<int:pk>', views.post_id, name='post_id'),
    path('mot-cat/(?P<cat_pk>[0-9]+)', views.MotivationalByCategory.as_view()),
    path('rev/', views.ReviewList.as_view()),
    path('review/rev-id/(?P<pk>[0-9]+)/', views.ReviewDescription.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('category/cat_idd/(?P<cat_pk>[0-9]+)', views.category_id),

    path('review_thread/<int:id>',views.review_thread,name='review_thread'),
    path('wishlist/<int:pk>',views.wishlist_motivation,name='wishlist'),
    path('user_wishlist',views.all_wishlist,name='all user wishlist picks'),
    path('profile/',views.profile, name='profile'),
    path('api/token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register', AuthUserRegistrationView.as_view(), name='register'),
    path('api/login', AuthUserLoginView.as_view(), name='login'),
    path('logout',AuthLogoutView.as_view(),name='logout'),
    path('subscribe/<int:pk>',views.subscription_service,name='category_subscription'),
    path('users', views.all_users, name='users'),
    path('remove_user/<int:id>',views.remove_user,name='user_deactivate'),
    path('review/<int:id>', views.review,  name = 'review'),
    path('current_user', views.current_user,name='current_user'),
    path('superuser/<int:pk>',views.change_to_superuser,name='superuser_status'),

]
