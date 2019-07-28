
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Role(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, default=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

# class UserRole(models.Model):
#     roles = models.CharField(blank=True, null=True,max_length=255)
#     def __unicode__(self):
#         return self.roles


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    county = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    # photo = models.ImageField(upload_to='uploads', blank=True)

    def __str__(self):
        return self.user
