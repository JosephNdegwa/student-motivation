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
    path('api/post/', views.post),
    path('api/post/mot_id/<int:pk>', views.post_id, name='post_id'),
    path('api/mot-cat/(?P<cat_pk>[0-9]+)', views.MotivationalByCategory.as_view()),
    path('api/rev/', views.ReviewList.as_view()),
    path('api/review/rev-id/(?P<pk>[0-9]+)/', views.ReviewDescription.as_view()),
    path('api/category/', views.CategoryList.as_view()),
    path('api/category/cat_idd/(?P<cat_pk>[0-9]+)', views.category_id),
    path('api/review_thread/<int:id>',views.review_thread,name='review_thread'),
    path('api/wishlist/<int:pk>',views.wishlist_motivation,name='wishlist'),
    path('api/user_wishlist',views.all_wishlist,name='all user wishlist picks'),
    path('api/profile/',views.profile, name='profile'),
    path('api/token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register', AuthUserRegistrationView.as_view(), name='register'),
    path('api/login', AuthUserLoginView.as_view(), name='login'),
    path('api/logout',AuthLogoutView.as_view(),name='logout'),
    path('api/subscribe/<int:pk>',views.subscription_service,name='category_subscription'),
    path('api/users', views.all_users, name='users'),
    path('api/remove_user/<int:id>',views.remove_user,name='user_deactivate'),
    path('api/review/<int:id>', views.review,  name = 'review'),
    path('api/current_user', views.current_user,name='current_user'),
    path('api/superuser/<int:pk>',views.change_to_superuser,name='superuser_status'),

]
