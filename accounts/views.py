from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Prefetch
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, DeleteView

from accounts.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from accounts.models import Profile
from photos.models import Photo

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


class UserLoginView(LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login-page.html'

    def get_success_url(self):
        return reverse_lazy('common:home_page')



class UserLogOutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('common:home_page')



class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/profile-details-page.html'
    context_object_name = 'profile'

    def get_queryset(self):
        return Profile.objects.select_related('user').prefetch_related('user__pets')


#Overwrite the get_context_data method to get the count of many to many related total photos count of all pets
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos_count = 0
        total_likes = 0

        for pet in self.object.user.pets.all():
            photos_count += pet.photos.count()
            for photo in pet.photos.all():
                total_likes += photo.likes.count()

        context['photos_count'] = photos_count
        context['total_likes'] = total_likes
        return context



class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('accounts:profile_details', kwargs={'pk': self.object.pk})



class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('common:home_page')

'''
To do:
Decide what happens when user deletes his profile. To delete the user and logout or create profile create functionality.
'''