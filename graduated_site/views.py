from django.shortcuts import render, HttpResponse, get_object_or_404, reverse, HttpResponseRedirect
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.contrib import messages
from .models import user_internship_post, survey_model
from .forms import survey_form, internship_form, adv_search, comment_form, company_form
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .decorators import is_post


@login_required
def survey(request):
    form = survey_form(data=request.GET or None)
    is_survey = survey_model.if_again_survey(request.user)
    if survey_model.if_again_survey(request.user) != True:
        if form.is_valid():
            created_form = form.save(commit=False)
            created_form.user = request.user
            created_form.save()
            msg = "You have successfully completed the form."
            messages.success(request, msg, extra_tags="success")
    return render(request, 'graduated_site/survey.html', context={'form': form,'is_survey':is_survey, 'page': 'survey'})


@login_required
def home_page(request):
    internship_posts = user_internship_post.objects.all()
    page = request.GET.get('page', 1)
    form = adv_search(data=request.GET or None)
    if form.is_valid():
        adv_type_search = form.cleaned_data.get('adv_type_search', None)
        search = form.cleaned_data.get('search', None)
        time_internship_search = form.cleaned_data.get('time_internship_search', None)
        period_internship_search = form.cleaned_data.get('period_internship_search', None)
        if search:
            internship_posts = internship_posts.filter(
                Q(content__icontains=search) | Q(title__icontains=search) | Q(user__first_name__icontains=search) | Q(
                    user__last_name__icontains=search) | Q(company__company_name__icontains=search) | Q(
                    working_area__area__icontains=search)).distinct()
        if adv_type_search and adv_type_search != 'all':
            internship_posts = internship_posts.filter(adv_type=adv_type_search)
            if time_internship_search and time_internship_search != 'all':
                internship_posts = internship_posts.filter(adv_type = adv_type_search).filter(time_internship= time_internship_search)
            if period_internship_search and period_internship_search != 'all':
                internship_posts = internship_posts.filter(adv_type= adv_type_search).filter(period_internship= period_internship_search)

    paginator = Paginator(internship_posts, 3)
    try:
        internship_posts = paginator.page(page)
    except EmptyPage:
        internship_posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        internship_posts = paginator.page(1)

    context = {'internship_posts': internship_posts, 'form': form, 'page': 'home'}
    return render(request, 'graduated_site/main.html', context)


@login_required
def internship_post_create(request):
    form = internship_form()
    if request.method == "POST":
        form = internship_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            internship_posts = form.save()
            internship_posts.user = request.user
            internship_posts.save()
            msg = "Your post named<strong> %s </strong>has been created" % (internship_posts.title)
            messages.success(request, msg, extra_tags="success")
            return HttpResponseRedirect(internship_posts.get_absolute_url())
    return render(request, 'graduated_site/post_create.html', context={'form': form, 'page': 'post_create'})


@login_required
def internship_post_delete(request, slug):
    internship_post = get_object_or_404(user_internship_post, slug=slug)
    if request.user != internship_post.user:
        return HttpResponseForbidden()
    internship_post.delete()
    msg = "Your post named<strong> %s </strong>has been deleted" % (internship_post.title)
    messages.success(request, msg, extra_tags="danger")
    return HttpResponseRedirect(reverse('home'))


@login_required
def internship_post_detail(request, slug):
    form = comment_form()
    internship_post = get_object_or_404(user_internship_post, slug=slug)
    context = {'internship_post': internship_post, 'form': form}
    return render(request, 'graduated_site/post_detail.html', context)


@login_required
@is_post
def add_comment(request, slug):
    internship_post = get_object_or_404(user_internship_post, slug=slug)
    form = comment_form(data=request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.post = internship_post
        new_comment.user = request.user
        new_comment.save()
        messages.success(request, 'Your comment has been created')
        return HttpResponseRedirect((internship_post.get_absolute_url()))


@login_required
def internship_post_update(request, slug):
    internship_post = get_object_or_404(user_internship_post, slug=slug)
    if request.user != internship_post.user:
        return HttpResponseForbidden()
    form = internship_form(instance=internship_post, data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        msg = "Your post named<strong> %s </strong>has been updated" % (internship_post.title)
        messages.success(request, msg, extra_tags="info")
        return HttpResponseRedirect(internship_post.get_absolute_url())
    context = {'internship_post': internship_post, 'form': form}
    return render(request, 'graduated_site/post_update.html', context=context)


@login_required
def company_add(request):
    form = company_form()
    if request.method == "POST":
        form = company_form(data=request.POST)
        if form.is_valid():
            created_company = form.save()
            msg = "<strong> %s </strong>company was added" % (created_company.company_name)
            messages.success(request, msg, extra_tags="success")
            return HttpResponseRedirect(reverse('home'))
    context = {'form': form}
    return render(request, 'graduated_site/company-add.html', context=context)
