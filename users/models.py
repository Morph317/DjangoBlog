from django.db import models
from django.contrib.auth.models import User #导入Django自带的用户类
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    bio = models.CharField(max_length=255,)
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('profile-detail', args=(str(self.user)))

@receiver(post_save, sender=User) #当 User 对象被创建或更新时，自动创建或更新对应的 Profile
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

