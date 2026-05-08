from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from accounts.forms import AppUserCreationForm, AppUserLoginForm

UserModel = get_user_model()


class UserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('common:home_page')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


##To do!
#Implement Login and Register Views
class UserLoginView(LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('common:home_page')
    
    def form_valid(self, form):
        super().form_valid(form)
        instance = ...



class UserLogOutView(LogoutView):
    success_url = reverse_lazy('common:home_page')

def profile_details(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-details-page.html')


def edit_profile(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-delete-page.html')