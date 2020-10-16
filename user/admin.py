from django.contrib import admin
from .models import User

class Users(admin.ModelAdmin):
    list_display = ('username','email','first_name','last_name','is_staff','is_active','date_joined','is_trusty','data_de_nascimento')
    list_display_links = ('username','email')
    serch_fields = ('id','username','email','first_name','last_name')
    list_per_page = 20

admin.site.register(User, Users)