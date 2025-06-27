from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Profile

class Command(BaseCommand):
    help = '为所有现有用户创建 Profile'

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            Profile.objects.get_or_create(
                user=user,
                defaults={'bio': 'Nothing here.'}
            )
        self.stdout.write(self.style.SUCCESS('成功为所有用户创建 Profile'))