from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import register_form, login_form, userprofile_update_form, user_work_company_form, message_box_form
from .models import UserProfile, user_work_company, user_message_box
from graduated_site.models import company
from graduated_site.decorators import anonymous_required
from graduated_site.models import user_internship_post
from follow.models import follow


# Create your views here.

@anonymous_required
def register(request):
    form = register_form(data=request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        username = form.cleaned_data.get('username')
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, '<b>Your account has been created</b>', extra_tags='success')
                return HttpResponseRedirect(reverse('user-login'))
    return render(request, 'auths/register.html', context={'form': form})


@anonymous_required
def user_login(request):
    form = login_form(data=request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get('password')
        username = form.cleaned_data.get('username')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                msg = "<b> %s welcome to the system</b>" % (user.userprofile.get_screen_name())
                messages.success(request, msg, extra_tags='success')
                return HttpResponseRedirect(reverse('home'))
    return render(request, 'auths/login.html', context={'form': form})

@login_required
def user_logout(request):
    username = request.user.username
    logout(request)
    msg = '<b>%s left the system </b>' % (username)
    messages.success(request, msg, extra_tags='success')
    return HttpResponseRedirect(reverse('user-login'))

@login_required
def user_profile(request, username):
    is_follow = False
    user = get_object_or_404(User, username=username)
    posts = user_internship_post.objects.filter(user=user)
    follower_and_followed = follow.user_follower_and_followed(user)
    follower = follower_and_followed['follower']
    followed = follower_and_followed['followed']

    if user != request.user:
        is_follow = follow.if_follow_user(follower=request.user, followed=user)

    return render(request, 'auths/user_profile.html',
                  context={'follower': follower, 'followed': followed, 'is_follow': is_follow, 'user': user,
                           'posts': posts, 'page': 'user_profile'})

@login_required
def user_profile_update(request):
    bio = request.user.userprofile.bio
    profile_photo = request.user.userprofile.profile_photo
    certificate = request.user.userprofile.certificate
    education = request.user.userprofile.education
    birth_date = request.user.userprofile.birth_date
    working_area = request.user.userprofile.working_area
    working_position = request.user.userprofile.working_position
    foreign_language = request.user.userprofile.foreign_language
    graduated_date = request.user.userprofile.graduated_date
    company_user = request.user.userprofile.company
    first_day = request.user.userprofile.company
    last_day = request.user.userprofile.last_day

    follower_and_followed = follow.user_follower_and_followed(request.user)
    follower = follower_and_followed['follower']
    followed = follower_and_followed['followed']
    initial = {'bio': bio, 'profile_photo': profile_photo, 'certificate': certificate, 'education': education,
               'birth_date': birth_date, 'working_area': working_area, 'working_position': working_position,
               'foreign_language': foreign_language, 'graduated_date': graduated_date, 'company_user': company_user,
               'first_day': first_day, 'last_day': last_day}
    form = userprofile_update_form(initial=initial, instance=request.user, data=request.POST or None,
                                   files=request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=True)
            bio = form.cleaned_data.get('bio', None)
            education = form.cleaned_data.get('education', None)
            profile_photo = form.cleaned_data.get('profile_photo', None)
            certificate = form.cleaned_data.get('certificate', None)
            birth_date = form.cleaned_data.get('birth_date', None)
            working_area = form.cleaned_data.get('working_area', None)
            working_position = form.cleaned_data.get('working_position', None)
            foreign_language = form.cleaned_data.get('foreign_language', None)
            graduated_date = form.cleaned_data.get('graduated_date', None)
            company_user = form.cleaned_data.get('company', None)
            first_day = form.cleaned_data.get('first_day', None)
            last_day = form.cleaned_data.get('last_day', None)

            user.userprofile.bio = bio
            user.userprofile.profile_photo = profile_photo
            user.userprofile.certificate = certificate
            user.userprofile.education = education
            user.userprofile.birth_date = birth_date
            user.userprofile.working_area = working_area
            user.userprofile.working_position = working_position
            user.userprofile.foreign_language = foreign_language
            user.userprofile.graduated_date = graduated_date
            user.userprofile.company = company_user
            user.userprofile.first_day = first_day
            user.userprofile.last_day = last_day
            user.userprofile.save()
            messages.success(request, 'Profile information updated', extra_tags='success')
            return HttpResponseRedirect(reverse('user-profile', kwargs={'username': user.username}))

    return render(request, 'auths/user_profile_update.html',
                  context={'follower': follower, 'followed': followed, 'form': form, 'page': 'profile_update'})

@login_required
def about_user(request, username):
    is_follow = False
    user = get_object_or_404(User, username=username)
    follower_and_followed = follow.user_follower_and_followed(user)
    follower = follower_and_followed['follower']
    followed = follower_and_followed['followed']

    if user != request.user:
        is_follow = follow.if_follow_user(follower=request.user, followed=user)

    return render(request, 'auths/about_user.html',
                  context={'follower': follower, 'followed': followed, 'is_follow': is_follow, 'user': user,
                           'page': 'about_user'})

@login_required
def user_work_company_view(request):
    form = user_work_company_form(data=request.POST or None)
    follower_and_followed = follow.user_follower_and_followed(request.user)
    follower = follower_and_followed['follower']
    followed = follower_and_followed['followed']
    if user_work_company.if_work_user(request.user) != True:
        if form.is_valid():
            created_form = form.save(commit=False)
            created_form.user = request.user
            created_form.save()
            msg = "<strong> %s </strong> company registration created" % (created_form.user.get_full_name())
            messages.success(request, msg, extra_tags="success")
    else:
        msg = "You are already working in a company"
        messages.success(request, msg, extra_tags="danger")

    return render(request, 'auths/work_company.html',
                  context={'follower': follower, 'followed': followed, 'form': form, 'page': 'work_company'})

@login_required
def user_message_box_view(request, username):
    user = get_object_or_404(User, username=username)
    n_message = user_message_box.if_message_box_open(request.user)
    message_title = ''
    message = ''
    message_user = ''
    if n_message == True:
        message_title = get_object_or_404(user_message_box, to_user=request.user).message_title
        message = get_object_or_404(user_message_box, to_user=request.user).message
        message_user = get_object_or_404(user_message_box, to_user=request.user).user

    form = message_box_form(data=request.POST or None)
    return render(request, 'auths/message_box.html',
                  context={'form': form, 'user': user, 'message': message, 'n_message':n_message, 'message_title': message_title,
                           'message_user': message_user, 'page': 'message-box'})

@login_required
def user_message_box_send_view(request, username):
    message = user_message_box.objects.all()

    form = message_box_form(data=request.POST or None)
    if form.is_valid():
        created_form = form.save(commit=False)
        created_form.user = request.user
        created_form.save()
        msg = "Your message has been sent"
        messages.success(request, msg, extra_tags="success")
        return HttpResponseRedirect(reverse('message-box', kwargs={'username': request.user.username}))
