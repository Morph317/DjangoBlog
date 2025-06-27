from django.urls import path
from .views import UserRegisterView, ProfileDetailView, UpdateProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/<str:username>', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/edit/<str:username>', UpdateProfileView.as_view(), name='edit-profile'),
]
