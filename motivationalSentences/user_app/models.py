from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/avatars', verbose_name='avatar', null=True , blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='uniq qode')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()

        return self.email
