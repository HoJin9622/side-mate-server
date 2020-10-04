import uuid
import time
import random
import string
from io import BytesIO

from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from service.utils import image as image_utils


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
        max_length=32,
        verbose_name='닉네임'
    )
    phone_number = models.CharField(
        null=True,
        blank=True,
        max_length=32,
        verbose_name='연락처'
    )
    position = models.CharField(
        null=True,
        blank=True,
        max_length=64,
        verbose_name='포지션'
    )
    profile_image = models.ImageField(
        upload_to='profile',
        null=True,
        blank=True,
        verbose_name='프로필 이미지',
    )

    def __str__(self):
        return f'{self.nickname}'

    @classmethod
    def generate_username(cls):
        return ''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(25)])

    def save(self, **kwargs):
        if self.profile_image and not self.profile_image.name.startswith('resized'):
            middle = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
            size = [500, 500]
            tmp = Image.open(BytesIO(self.profile_image.read()))
            image = image_utils.rotate(tmp)
            self.profile_image = image_utils.make_thumbnail(size, image, self.profile_image.name)
            self.profile_image.name = f'resized_{middle}_{int(time.time() * 100)}.{self.profile_image.name.split(".")[-1]}'
            # self.profile_image.name = self.profile_image.name.replace("JPG", "jpg")
