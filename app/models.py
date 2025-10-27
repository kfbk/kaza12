from django.db import models

# class Department(models.Model):
#     name = models.CharField(max_length=30)


# class Student(models.Model):
#     name = models.CharField(max_length=30)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Category(models.Model):
  name = models.CharField( max_length=30)
  def __str__(self):
    return self.name

class Cooking(models.Model):
    name = models.CharField('料理', max_length=100)
    description = models.TextField('説明', default="", blank=True)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    sequence = models.IntegerField(default=0)        # 表示順
    price = models.IntegerField(default=0) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# お知らせ
class Post(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
