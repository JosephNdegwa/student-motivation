from .models import Category, StudentUser,Post,Review,Profile, Subscription, WishList,Category,ReviewThread
from rest_framework import fields, serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .email import send_welcome_email



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = (
            'username',
            'email',
            'role',
            'password'
        )

    def create(self, validated_data):
        auth_user = StudentUser.objects.create_user(**validated_data)
        return auth_user

class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = (
            'is_superuser',
        )

class ActiveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = (
            'is_active',
        )

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = (
            'first_name',
            'last_name'
        )
    


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login details")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)


            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'username': user.username,
                'role': user.role,
            }

            return validation
        except StudentUser.DoesNotExist:
            raise serializers.ValidationError("Invalid login details")

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'role',
            'is_active',
            'is_staff',
            'is_superuser',
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name')

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault(), source="user.username",)
    category = CategorySerializer( read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user','profile_photo','category','profile_email','phone_number', 'created_at')




class PostPostSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'blog', 'video', 'title', 'category', 'description', 'profile', 'created_at')


class PostSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    category = CategorySerializer( read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'blog', 'video', 'title', 'category', 'description', 'profile', 'pub_at')

class ReviewSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    post= PostSerializer(read_only = True)
    class Meta:
        model = Review
        fields = ('id', 'review', 'profile', 'post', 'pub_at')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name')

class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault(), source="user.username",)
    category = CategorySerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault(), source="user.username",)
    class Meta:
        model= Subscription
        fields = ('id','user','category')

        def save(self):
            name = self.validated_data['name']
            email = self.validated_data['email']
            send_welcome_email(name=name, receiver=email)

class ReviewThreadSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True)
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = ReviewThread
        fields = ('id','review','profile','content','posted_at')


class WishListSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = WishList
        fields = ('profile','post')