from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'gender', 'image']


class UserUpdatingForm(UserChangeForm):

    class Meta:
        model = User
        fields = '__all__'