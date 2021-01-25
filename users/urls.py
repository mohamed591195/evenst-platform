from django.urls import path
from .views import UserRegistrationView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register_view'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login_view'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout_view')
]