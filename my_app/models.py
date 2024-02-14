from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {
    'blank': True,
    'null': True,
}


class Post(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    preview = models.ImageField(upload_to='images/', **NULLABLE, verbose_name='Превью')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name="Время публикации", **NULLABLE)
    is_publish = models.BooleanField(default=True, verbose_name="Опубликовано")
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
