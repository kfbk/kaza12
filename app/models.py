from django.db import models

class Cooking(models.Model):
    name = models.CharField('料理', max_length=100)
    description = models.TextField('説明', default="", blank=True)
    image = models.ImageField(upload_to='media', verbose_name='イメージ画像', null=True, blank=True)

    def __str__(self):
        return self.name

# お知らせ
class Post(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
