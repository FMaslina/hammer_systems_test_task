from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.


class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона", unique=True)
    first_name = models.TextField(verbose_name="Имя")
    last_name = models.TextField(verbose_name="Фамилия")
    username = models.CharField(max_length=100, verbose_name="Юзернейм", unique=True)
    referral_code = models.CharField(max_length=6, verbose_name="Реферральный код", unique=True)
    invite_code = models.CharField(max_length=6, verbose_name="Код пригласившего", blank=True, null=True)

    USERNAME_FIELD = "phone_number"
