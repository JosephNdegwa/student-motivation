from django.contrib import admin

from motivation.models import Post, Staff, Student

# Register your models here.
admin.site.register(Staff)
admin.site.register(Student)

admin.site.register(Post)
