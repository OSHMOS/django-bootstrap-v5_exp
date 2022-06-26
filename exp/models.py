from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=20, verbose_name="제목")
    content = models.TextField(verbose_name="내용")

    def __str__(self):
        return self.title
