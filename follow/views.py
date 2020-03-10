from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, Http404
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .models import follow

# Create your views here.

def follow_system(request):
    if not request.is_ajax():
        return HttpResponseBadRequest

    data={'html': '', 'is_valid':True, 'msg': '<b>Unfollow</b>'}
    follower_username= request.GET.get('follower_username', None)
    followed_username= request.GET.get('followed_username', None)

    follower = get_object_or_404(User, username=follower_username)
    followed = get_object_or_404(User, username=followed_username)

    is_follow = follow.if_follow_user(follower = follower, followed = followed)

    if not is_follow:
        follow.follow_user(follower=follower, followed= followed)
    else:
        follow.dont_follow_user(follower=follower, followed=followed)
        data.update({'msg': '<b>Follow</b>'})

    n_follower_and_followed = follow.user_follower_and_followed(followed)
    context={'user': followed, 'follower': n_follower_and_followed['follower'], 'followed': n_follower_and_followed['followed']}
    html = render_to_string('auths/profile/n_follow_include.html', context=context, request=request)
    data.update({'html': html})

    return JsonResponse(data=data)

def follower_and_followed_list(request, follow_type):
    data={'is_valid':True, 'html': ''}
    username = request.GET.get('username', None)
    if not username:
        raise Http404

    user = get_object_or_404(User, username=username)
    if follow_type=='follower':
        followers = follow.get_followed(user=user)
        html=render_to_string('auths/follow/follower_and_followed_list.html', context={'follow': followers, 'follow_type': follow_type},request=request)

    elif follow_type=='followed':
        followed = follow.get_followers(user=user)
        html = render_to_string('auths/follow/follower_and_followed_list.html', context={'follow': followed, 'follow_type': follow_type},
                                request=request)

    else:
        raise Http404

    data.update({'html': html})
    return JsonResponse(data=data)