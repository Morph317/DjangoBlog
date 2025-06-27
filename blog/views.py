from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404, render, redirect

#def HomeView(request):
#    return render(request, "home.html", {})
#Django标签用法：
#{% if database -%}{{ database.name }}{%- else -%}blah{%- endif %}

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = "-date"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = 'users/login/'
    model = Post
    form_class = PostForm
    template_name = "post_form.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    #fields = ("title", "body")

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "update_post.html"

class DeletePostView(UpdateView): #删除后会将该Post的属性visible改为false
    model = Post
    template_name = "delete_post.html"
    fields = ("is_visible",)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.is_visible = False
        post.save()
        return redirect('home')