from django.contrib import admin
from .models import user_internship_post,working_area,comment,company ,survey_model

admin.site.register(user_internship_post)
admin.site.register(working_area)
admin.site.register(comment)
admin.site.register(company)
admin.site.register(survey_model)

