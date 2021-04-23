# accounts/urls.py
from django.urls import path

from accounts import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/',views.login,name='login'),
]