from django.contrib.gis.db import models


class City(models.Model):
    class Meta:
        verbose_name = '도시'
        verbose_name_plural = verbose_name

    name = models.CharField(
        verbose_name='도시명',
        max_length=32,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.name}'


class Region(models.Model):
    class Meta:
        verbose_name = '세부지역'
        verbose_name_plural = verbose_name

    city = models.ForeignKey(
        to=City,
        verbose_name='도시',
        related_name='regions',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='지역명',
        max_length=32,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    class Meta:
        verbose_name = '게시물'
        verbose_name_plural = verbose_name

    STATUS = (
        ('hiring', '모집 중'),
        ('end', '모집 완료')
    )
    user = models.ForeignKey(
        to='User',
        verbose_name='작성자',
        related_name='posts',
        on_delete=models.CASCADE,
    )
    region = models.ForeignKey(
        null=True,
        to='Region',
        verbose_name='지역',
        related_name='posts',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        null=True,
        verbose_name='제목',
        max_length=64,
    )
    content = models.TextField(
        null=True,
        verbose_name='내용',
    )
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default=STATUS[0][0],
        verbose_name='상태',
    )
    hire_limit = models.PositiveIntegerField(
        null=True,
        verbose_name='모집인원',
    )
    start_time = models.DateField(
        verbose_name='시작 날짜',
        auto_now=True
    )
    end_time = models.DateField(
        verbose_name='예상 종료 날짜',
        auto_now=True
    )
    favorite_users = models.ManyToManyField(
        to='User',
        related_name='favorite_users',
        verbose_name='즐겨찾기한 사람들',
    )
    favorite_count = models.PositiveIntegerField(
        verbose_name='즐겨찾기 수',
        default=0
    )
    created_at = models.DateField(
        verbose_name='작성일',
        auto_now=True
    )

    def __str__(self):
        return f'{self.user}/{self.title}'

