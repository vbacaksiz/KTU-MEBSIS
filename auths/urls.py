from django.urls import path, re_path
from .views import register, user_login, user_logout, user_profile,user_profile_update,about_user,user_work_company_view, user_message_box_view, user_message_box_send_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('user-update/', user_profile_update, name='user-update'),
    path('work-company/', user_work_company_view, name='work-company'),
    re_path(r'^(?P<username>[-\w]+)/$', user_profile, name='user-profile'),
    re_path(r'^(?P<username>[-\w]+)/about/$', about_user, name='about-user'),
    re_path(r'^(?P<username>[-\w]+)/message-box/$', user_message_box_view, name='message-box'),
    re_path(r'^(?P<username>[-\w]+)/message-box-send/$', user_message_box_send_view, name='message-box-send'),
]
