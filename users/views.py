from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
from django.urls import reverse


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    context_object_name = "profile"

    def get_object(self):
        # 根据 URL 中的 username 获取对应的 User
        user = get_object_or_404(User, username=self.kwargs["username"])
        # 返回关联的 Profile 对象
        return user.profile

class UpdateProfileView(generic.UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "update_profile.html"
    context_object_name = "profile"

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs["username"])
        return user.profile

    def get_success_url(self):
        # 获取更新后的 Profile 关联的 User 的用户名
        username = self.object.user.username
        # 反向解析到 profile_detail，传递 username 参数
        return reverse("profile-detail", kwargs={"username": username})