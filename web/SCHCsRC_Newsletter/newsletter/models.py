from django.db import models
from django.conf import settings

import uuid
import os


class trends_Post(models.Model):
    def delete(self, *args, **kargs):
        if self.thumbnail:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.thumbnail.path))
        super(trends_Post, self).delete(*args, **kargs)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='게시글 ID')
    title = models.CharField(max_length=50, verbose_name='제목')
    views = models.PositiveIntegerField(default=0, verbose_name='조회수')
    author = models.CharField(max_length=10, verbose_name='작성자')
    content = models.TextField(verbose_name='내용')
    thumbnail = models.ImageField(null=True, upload_to="thumbnails/%Y/%m/%d", verbose_name='썸네일 경로')
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    modified_datetime = models.DateTimeField(null=True, verbose_name='수정 날짜')
    is_valid = models.BooleanField(default=1, verbose_name='게시글 유효성')


class reports_Post(models.Model):
    def delete(self, *args, **kargs):
        if self.thumbnail:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.thumbnail.path))
        super(reports_Post, self).delete(*args, **kargs)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='게시글 ID')
    title = models.CharField(max_length=50, verbose_name='제목')
    views = models.PositiveIntegerField(default=0, verbose_name='조회수')
    author = models.CharField(max_length=10, verbose_name='작성자')
    content = models.TextField(verbose_name='내용')
    thumbnail = models.ImageField(null=True, upload_to="thumbnails/%Y/%m/%d", verbose_name='썸네일 경로')
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    modified_datetime = models.DateTimeField(null=True, verbose_name='수정 날짜')
    is_valid = models.BooleanField(default=1, verbose_name='게시글 유효성')


class projects_Post(models.Model):
    def delete(self, *args, **kargs):
        if self.thumbnail:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.thumbnail.path))
        super(projects_Post, self).delete(*args, **kargs)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='게시글 ID')
    title = models.CharField(max_length=50, verbose_name='제목')
    views = models.PositiveIntegerField(default=0, verbose_name='조회수')
    author = models.CharField(max_length=10, verbose_name='작성자')
    content = models.TextField(verbose_name='내용')
    thumbnail = models.ImageField(null=True, upload_to="thumbnails/%Y/%m/%d", verbose_name='썸네일 경로')
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    modified_datetime = models.DateTimeField(null=True, verbose_name='수정 날짜')
    is_valid = models.BooleanField(default=1, verbose_name='게시글 유효성')

class trends_PostImage(models.Model):
    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(trends_PostImage, self).delete(*args, **kargs)
    post = models.ForeignKey(trends_Post, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to=f"images/%Y/%m/%d", verbose_name='이미지 경로')


class reports_PostImage(models.Model):
    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(reports_PostImage, self).delete(*args, **kargs)
    post = models.ForeignKey(reports_Post, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to=f"images/%Y/%m/%d", verbose_name='이미지 경로')


class projects_PostImage(models.Model):
    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(projects_PostImage, self).delete(*args, **kargs)
    post = models.ForeignKey(projects_Post, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to=f"images/%Y/%m/%d", verbose_name='이미지 경로')
