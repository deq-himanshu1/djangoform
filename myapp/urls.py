from django.urls import path
from .views import user_profile_view, success_view

urlpatterns = [
    path('user_profile/', user_profile_view, name='user_profile'),
    path('success/', success_view, name='success'),
]