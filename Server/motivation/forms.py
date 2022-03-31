from django import forms
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User
from . import models
class StaffUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_("Please input a valid username"))
        if not password:
            raise ValueError(_("Please a Password"))
        username = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 1)
        if extra_fields.get('role') != 1:
            raise ValueError('Admin is Superuser')
        new_user = self.create_user(username, password, **extra_fields,is_superuser=True)
        new_user.is_admin = True
        new_user.is_staff = True
        new_user.save()

        return new_user