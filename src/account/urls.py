from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import UserLoginView, UserRegisterView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='account:login'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
