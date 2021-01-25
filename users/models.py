from django.db import models
from django.db.utils import cached_property
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('Email field is required !')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user


    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if not extra_fields['is_superuser']:
            raise ValueError('is_superuser must be True for superusers')

        if not extra_fields['is_staff']:
            raise ValueError('is_staff must be True for superusers')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    
    image = models.ImageField('Personal Image', upload_to='profiles/images', blank=True)

    gender = models.CharField(choices=GENDER_CHOICES, max_length=3, blank=True)

    email = models.EmailField(unique=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    @property
    def is_admin(self):
        return self.is_superuser

    @cached_property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()

