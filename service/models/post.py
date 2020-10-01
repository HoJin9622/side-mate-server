from django.contrib.gis.db import models


class Post(models.Model):
    class Meta:
        verbose_name = '게시물',
        verbose_name_plural = verbose_name

    user = models.ForeignKey(
        to='User',
        related_name='posts',
        on_delete=models.CASCADE,
        verbose_name='작성자'
    )
