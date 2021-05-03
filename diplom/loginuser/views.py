from django.shortcuts import render
from django.views.generic import View, DetailView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import LoginForm, UserUpdateForm


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'loginuser/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('documents/tenders/')
        return render(request, 'loginuser/login.html', {'form': form})


class ProfileView(DetailView):
    model = User
    template_name = 'loginuser/profile.html'


class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "loginuser/update_profile.html"
    success_url = "/"



