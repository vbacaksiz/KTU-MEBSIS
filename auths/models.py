from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from graduated_site.models import company


# Create your models here.


class UserProfile(models.Model):
    working_position_choice = (('INTERN', 'INTERN'), ('MANAGER', 'MANAGER'), ('PROGRAMMER', 'PROGRAMMER'), ('TECHNICIAN', 'TECHNICIAN'))
    working_area_choice = (('ARTIFICAL INTELLIGENCE', 'ARTIFICAL INTELLIGENCE'), ('SOUND PROCESSING', 'SOUND PROCESSING'), ('IMAGE PROCESSING', 'IMAGE PROCESSING'), ('COMPUTER FORENSICS', 'COMPUTER FORENSICS'))
    user = models.OneToOneField(User, null=True, blank=False, verbose_name='User', on_delete=models.PROTECT)
    bio = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Biography')
    profile_photo = models.ImageField(null=True, blank=True, verbose_name='Profile Photo')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Birthdate')
    working_area = models.CharField(max_length=25, choices=working_area_choice, null=True, blank=True, verbose_name='Working Area')
    working_position = models.CharField(max_length=25, choices=working_position_choice, null=True, blank=True, verbose_name='Working Position')
    foreign_language = models.CharField(max_length=500, null=True, blank=True, verbose_name='Foreign Languages')
    certificate = models.CharField(max_length=500, null=True, blank=True, verbose_name='Certificate')
    education = models.CharField(max_length=500, null=True, blank=True, verbose_name='Education')
    graduated_date = models.DateField(null=True, blank=True, verbose_name='Graduated Date')
    company = models.ForeignKey(company, max_length=25, null=True, blank=True, verbose_name='Company', on_delete=models.CASCADE)
    first_day = models.DateField(null=True, blank=True, verbose_name='Your First Day In Company')
    last_day = models.DateField(null=True, blank=True, verbose_name='Your Last Day In Company')


    class Meta:
        verbose_name_plural = 'User Profiles'

    def get_screen_name(self):
        user = self.user
        if user.get_full_name():
            return user.get_full_name()
        return user.username

    def get_user_profile_url(self):
        url = reverse('user-profile', kwargs={'username': self.user.username})
        return url

    def get_profile_photo(self):
        if self.profile_photo:
            return self.profile_photo.url
        return "/static/img/default.jpg"

    def __str__(self):
        return "%s Profile" % (self.get_screen_name())



class user_work_company(models.Model):

    user = models.ForeignKey(User, null=True, blank=True, verbose_name='User', on_delete=models.CASCADE)
    company = models.ForeignKey(company, null=True, blank=False, verbose_name='Company', on_delete=models.CASCADE)
    first_day = models.CharField(max_length=25, null=True, blank=False, verbose_name='Your First Day In Company')

    class Meta:
        verbose_name_plural='Work Company'

    def __str__(self):
        return "%s %s"%(self.company, self.user)

    @classmethod
    def if_work_user(cls, user):
        return cls.objects.filter(user = user).exists()

class user_message_box(models.Model):

    user = models.ForeignKey(User, null=True, blank=True, verbose_name='User',related_name='sending_user', on_delete=models.PROTECT)
    to_user = models.ForeignKey(User, null=True, blank=False, verbose_name='Message To User',related_name='sent_user', on_delete=models.CASCADE)
    message_title = models.CharField(max_length=25, null=True, blank=False, verbose_name='Message Title')
    message = models.CharField(max_length=500, null=True, blank=False, verbose_name='Message')

    class Meta:
        verbose_name_plural="Messages"

    def __str__(self):
        return "%s %s"%(self.user, self.to_user)

    @classmethod
    def if_message_box_open(cls, user):
        return cls.objects.filter(to_user=user).exists()



