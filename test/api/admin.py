from django.contrib import admin
from django.contrib.auth.models import User
from api.models import *


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('first_name','last_name','last_login','date_joined','email', 'is_superuser')
    #list_filter = ('city',)
    list_display = ('first_name','last_name','last_login','date_joined','email','is_superuser')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('description','admin_thumbnail')

#unRegister the defuaut setup of User model on admin to add custom User model register
admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
admin.site.register(Image_Display, ImageAdmin)
