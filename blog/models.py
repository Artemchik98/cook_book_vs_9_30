from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published'),
    )
    title=models.CharField(max_length=250,verbose_name='Название поста')
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User,on_delete=models.CASCADE,
                         related_name='blog_posts',verbose_name='Автор')
    short_description=models.CharField(max_length=400,verbose_name='Короткое описание')
    publish=models.DateTimeField(default=timezone.now,verbose_name='Дата публикации')

