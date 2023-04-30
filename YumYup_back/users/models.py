from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, login, password=None, email=None, phone_number=None, bio=None, avatar=None, **extra_fields):
        if not login:
            raise ValueError('The Login field must be set')
        user = self.model(
            login=login,
            email=self.normalize_email(email),
            phone_number=phone_number,
            bio=bio,
            avatar=avatar,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password, email=None, phone_number=None, bio=None, avatar=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(login, password, email, phone_number, bio, avatar, **extra_fields)


class User(AbstractBaseUser):
    login = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'login'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.login