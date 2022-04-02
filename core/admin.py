from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ['full_name','relationship','email','phone_number','address',]