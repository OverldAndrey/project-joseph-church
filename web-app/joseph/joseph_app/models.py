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
        user.save(using=self._db)
        return user


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
    avatar = models.CharField(max_length=255)
    date_of_birth = models.DateField(default="1970-01-01")
    phone = models.CharField(max_length=18)
    pubnet = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    course = models.IntegerField(default=1)
    reg_address = models.CharField(max_length=255)
    cur_address = models.CharField(max_length=255)
    organizations = models.CharField(max_length=1023)
    hobby = models.CharField(max_length=1023)
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



# Create your models here.
