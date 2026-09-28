from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
from django.utils.text import slugify
from django.shortcuts import reverse

# Create your models here.

class Post(models.Model):

    post_name = models.CharField(max_length=255, verbose_name='Название поста')
    date_published = models.DateField(verbose_name='Дата публикации')
    post_text = RichTextUploadingField(blank=True, null=True, verbose_name='Текст поста')
    post_image = models.ImageField(upload_to='media/', verbose_name='Картинка поста', blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name='Опубликовать.')

    post_slug = models.SlugField(unique=True, verbose_name='Ссылка на пост')

    def get_absolute_url(self):
        return f'/blog/{self.post_slug}/'
    
    def __str__(self):
        return self.post_name
    
    class Meta:

        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'



    
