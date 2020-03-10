from django.db import models
from django.shortcuts import reverse
from unidecode import unidecode
from django.template.defaultfilters import slugify
from uuid import uuid4
import os
from django.contrib.auth.models import User


def upload_to(instance, filename):
    extension = filename.split('.')[-1]
    new_name = "%s.%s" % (str(uuid4()), extension)
    unique_id = instance.unique_id
    return os.path.join('media_root', unique_id, new_name)


class working_area(models.Model):
    area = models.CharField(max_length=50, verbose_name='Workspace')

    class Meta:
        verbose_name_plural = 'Workspace'

    def __str__(self):
        return self.area


class company(models.Model):
    phone_number = models.CharField(max_length=11, verbose_name='Phone Number', blank=False, null=True)
    adress = models.CharField(max_length=200, verbose_name='Adress', blank=False, null=True)
    company_name = models.CharField(max_length=25, verbose_name='Company Name', blank=False, null=True)
    company_type = models.CharField(max_length=25, verbose_name='Company Type', blank=False, null=True)
    company_sector = models.ManyToManyField(to=working_area, blank=False, related_name='sector',
                                            verbose_name='Company Industry',
                                            help_text='Select the workspaces.(Multiple selectable.)')

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return "%s" % (self.company_name)


class user_internship_post(models.Model):
    ad_type = ((None, 'Please select ad type'), ('0', 'INTERN'), ('1', 'WORK'))
    period_internship_choice = (
        (None, 'Please select internship period'), ('SUMMER', 'SUMMER'), ('SPRING', 'SPRING'), ('WINTER', 'WINTER'), ('AUTUMN', 'AUTUMN'))
    time_internship_choice = ((None, 'Please select internship duration'), ('30 DAYS', '30 DAYS'), ('60 DAYS', '60 DAYS'))

    company = models.ForeignKey(company, null=True, verbose_name='Select Company', on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, verbose_name='User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=True, verbose_name="Title",
                             help_text='Enter the title of the post.')
    image = models.ImageField(upload_to=upload_to, blank=True, null=True, verbose_name='Photo',
                              help_text='You can add photo.')
    content = models.CharField(max_length=1000, blank=False, null=True, verbose_name="Content",
                               help_text='Enter the content of the post.')
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    adv_type = models.CharField(max_length=10, choices=ad_type, blank=False, null=True,
                                verbose_name='Select Ad Type')
    period_internship = models.CharField(max_length=25, choices=period_internship_choice, null=True, blank=True,
                                         verbose_name='Internship Period')
    time_internship = models.CharField(max_length=25, choices=time_internship_choice, null=True, blank=True,
                                       verbose_name='Internship Duration')
    deadline = models.DateField(blank=False, null=True, verbose_name='Deadline')
    slug = models.SlugField(null=True, unique=True, editable=False)
    unique_id = models.CharField(max_length=100, editable=True, null=True)
    working_area = models.ManyToManyField(to=working_area, blank=True, related_name='Workspace',
                                          verbose_name='Workspace',
                                          help_text='Choose the workspace you want.(Multiple selectable.)')

    class Meta:
        verbose_name_plural = 'Announcements'
        ordering = ['deadline']

    def __str__(self):
        return "%s %s" % (self.title, self.user)

    def get_ad_type_html(self):
        if self.adv_type == '0':
            return '<span class="label label-{1}">{0}</span>'.format(self.get_adv_type_display(),
                                                                     'info')
        return '<span class="label label-{1}">{0}</span>'.format(self.get_adv_type_display(),
                                                                 'primary')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return None

    def get_unique_slug(self):
        num = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while user_internship_post.objects.filter(slug=new_slug).exists():
            num += 1
            new_slug = "%s-%s" % (slug, num)

        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            new_unique_id = str(uuid4())
            self.unique_id = new_unique_id
            self.slug = self.get_unique_slug()
        else:
            post = user_internship_post.objects.get(slug=self.slug)
            if user_internship_post.title != self.title:
                self.slug = self.get_unique_slug()

        super(user_internship_post, self).save(*args, **kwargs)

    def get_post_comment(self):
        return self.comment.all()


class survey_model(models.Model):
    graduated_program_choices = (
        (None, 'Please select the program you graduated from'), ('Undergraduate 1.Education', 'Undergraduate 1.Education'),
        ('Undergraduate 2.Education', 'Undergraduate 2.Education'), ('Graduate', 'Graduate'), ('Doctorate', 'Doctorate'))
    graduated_state_choices = ((None, 'Please select your graduation status'), ('New Graduated', 'New Graduated'),
                               ('Graduated in the past year', 'Graduated in the past year'))
    user = models.ForeignKey(User, null=True, verbose_name='User', on_delete=models.CASCADE)
    name_surname = models.CharField(max_length=50, null=True, blank=False, verbose_name='Name Surname *')
    graduated_year = models.CharField(max_length=4, null=True, blank=False, verbose_name='Graduation Year *')
    email = models.EmailField(max_length=50, null=True, blank=False, verbose_name='E-mail *')
    phone_number = models.CharField(max_length=12, null=True, blank=False, verbose_name='Phone Number *')
    graduated_program = models.CharField(max_length=30, choices=graduated_program_choices, null=True, blank=True, verbose_name='The Program You Graduated From')
    adress = models.CharField(max_length=100, null=True, blank=True, verbose_name='Adress')
    social_profile = models.CharField(max_length=50, null=True, blank=True,
                                      verbose_name='Your Social Media Profile Page')
    graduated_state = models.CharField(max_length=30, choices=graduated_state_choices, null=True, blank=True, verbose_name='Graduation Status')

    class Meta:
        verbose_name_plural = 'Surveys'

    def __str__(self):
        return "%s %s" % (self.user, self.email)

    @classmethod
    def if_again_survey(cls, user):
        return cls.objects.filter(user=user).exists()


class comment(models.Model):
    user = models.ForeignKey(User, null=True, related_name='comment', on_delete=models.CASCADE)
    post = models.ForeignKey(user_internship_post, null=True, related_name='comment', on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=False, verbose_name='Comment', max_length=500)
    comment_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return "%s %s" % (self.user, self.post)

    def get_screen_name(self):
        if self.user.first_name:
            return "%s" % (self.user.get_full_name())
        return self.user.username
