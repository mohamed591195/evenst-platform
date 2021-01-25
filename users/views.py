from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm
from django.contrib.auth import login


class UserRegistrationView(FormView):

    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = '/'

    def form_valid(self, form):

        user = form.save()

        login(self.request, user)

        return super().form_valid(form)
