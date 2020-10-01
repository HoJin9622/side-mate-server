import uuid
import random

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = verbose_name

    username_validator = UnicodeUsernameValidator()

    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )
    username = models.CharField(
        verbose_name='아이디',
        unique=True,
        max_length=128,
        # help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        # help_text=_('6자의 문자, 숫자 그리고 @/./+/-/_만 가능합니다.'),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists."), },
    )
    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name='이메일'
    )
    nickname = models.CharField(
        null=True,
        max_length=30,
        verbose_name='닉네임'
    )
    phone_number = models.CharField(
        null=True,
        max_length=15,
        verbose_name='연락처'
    )
    # is_approved = models.BooleanField(
    #     verbose_name='관리자 승인',
    #     default=False
    # )

    def __str__(self):
        return f'{self.nickname}'

    @classmethod
    def generate_username(cls):
        return ''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(25)])

    def __str__(self):
        return f'{self.nickname}/{self.phone_number}'

