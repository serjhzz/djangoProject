from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'blank': True,
    'null': True,
}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    email_verified = models.BooleanField(default=False, verbose_name='Почта подтверждена')
    email_verification_token = models.CharField(max_length=255, **NULLABLE)

    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    telegram = models.CharField(max_length=150, verbose_name='Telgram', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
