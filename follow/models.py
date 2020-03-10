from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class follow(models.Model):
    follower = models.ForeignKey(User, null=True, related_name='follower', verbose_name='Follower User', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, null=True, related_name='followed', verbose_name='Followed User', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Following System'

    def __str__(self):
        return "Follower {} - Followed {}".format(self.follower.username, self.followed)

    @classmethod
    def follow_user(cls, follower, followed):
        cls.objects.create(follower=follower, followed=followed)

    @classmethod
    def dont_follow_user(cls, follower, followed):
        cls.objects.filter(follower=follower, followed=followed).delete()

    @classmethod
    def if_follow_user(cls, follower, followed):
        return cls.objects.filter(follower = follower, followed = followed).exists()

    @classmethod
    def user_follower_and_followed(cls, user):
        data = {'follower': 0, 'followed':0}
        follower = cls.objects.filter(follower = user).count()
        followed = cls.objects.filter(followed = user).count()

        data.update({'follower': follower, 'followed': followed})
        return data

    @classmethod
    def get_followers(cls, user):
        return cls.objects.filter(followed=user)

    @classmethod
    def get_followed(cls, user):
        return cls.objects.filter(follower=user)