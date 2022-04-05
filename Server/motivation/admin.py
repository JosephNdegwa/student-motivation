from django.contrib import admin
from motivation.models import StudentUser,Category,Review,Post,WishList,ReviewThread,Profile 

# Register your models here.
admin.site.register(StudentUser)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Post)
admin.site.register(WishList)
admin.site.register(ReviewThread)
admin.site.register(Profile)



