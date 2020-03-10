from django.urls import path, re_path
from .views import follow_system, follower_and_followed_list

urlpatterns = [
    path('follow-system/', follow_system, name='follow-system'),
    re_path(r'^follower-and-follower-list/(?P<follow_type>[-\w]+)/$', follower_and_followed_list, name='follower-and-followed-list'),
]
