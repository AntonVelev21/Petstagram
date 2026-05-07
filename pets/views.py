from django.db.models import Prefetch
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from pets.models import Pet
from photos.models import Photo


class AddPetView(CreateView):
    model = Pet
    form_class = PetCreateForm
    success_url = reverse_lazy('accounts:profile_details', kwargs={'pk': 1})
    template_name = 'pets/pet-add-page.html'



class DeletePetView(DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/pet-delete-page.html'
    success_url = reverse_lazy('accounts:profile_details', kwargs={'pk': 1})
    slug_url_kwarg = 'pet_slug'

    def get_initial(self):
        return self.object.__dict__



class PetDetailsView(DetailView):
    model = Pet
    context_object_name = 'pet'
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'


    def get_queryset(self):
        return Pet.objects.prefetch_related(
            Prefetch(
                'photo_set',
                queryset=Photo.objects.prefetch_related('likes', 'comments', 'tagged_pets')
            )
        )




class EditPetView(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse_lazy('pets:pet_details', kwargs={'username': self.kwargs['username'],
                                                        'pet_slug': self.kwargs['pet_slug']})

