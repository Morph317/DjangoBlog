from django.db import models
from django.contrib.auth.models import User #导入Django自带的用户类
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=2) #ForeignKey可以连接数据库中其它model
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title + "-" + str(self.author) #__str__是在print该类时会输出的字符，用来增加可读性
    
#    def get_absolute_url(self):
#        return reverse('post-detail', args=(str(self.pk)))

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})