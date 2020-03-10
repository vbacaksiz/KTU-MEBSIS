from django.urls import path, re_path
from .views import home_page, internship_post_create, internship_post_delete, internship_post_update, survey, internship_post_detail,add_comment,company_add


urlpatterns = [
    path('', home_page, name='home'),
    path('post-create/', internship_post_create, name='post-create'),
    path('graduated-survey/', survey, name='survey'),
    re_path(r'^post-delete/(?P<slug>[-\w]+)/$', internship_post_delete, name='post-delete'),
    re_path(r'^post-update/(?P<slug>[-\w]+)/$', internship_post_update, name='post-update'),
    re_path(r'^post-detail/(?P<slug>[-\w]+)/$', internship_post_detail, name='post-detail'),
    re_path(r'^add-comment/(?P<slug>[-\w]+)/$', add_comment, name='add-comment'),
    path('add-company/', company_add, name='add-company'),
]
