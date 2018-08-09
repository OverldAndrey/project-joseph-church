from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

import datetime

class NewUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have username!")

        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


def upload_avatar(instance, filename):
    return "{0}/avatar/{1}".format(instance.user.pk, filename)

class User(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = datetime.datetime.now()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=127)
    date_of_birth = models.DateField(default="1970-01-01")
    phone = models.CharField(max_length=18)
    pubnet = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    course = models.IntegerField(default=1)
    reg_address = models.CharField(max_length=255)
    cur_address = models.CharField(max_length=255)
    organizations = models.TextField()
    hobby = models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = NewUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Poll(models.Model):
    text = models.CharField(max_length=16383)
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    poll_image = models.CharField(max_length=127, default=" ")
    poll_type = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.text

class Poll_choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text

class User_poll_choice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.IntegerField(default=0)
    choice = models.IntegerField(default=0)

    def __str__(self):
        return self.user.email+" "+str(self.poll)+" "+str(self.choice)




# Create your models here.