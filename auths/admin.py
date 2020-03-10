from django.contrib import admin
from .models import UserProfile, user_work_company, user_message_box

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(user_work_company)
admin.site.register(user_message_box)