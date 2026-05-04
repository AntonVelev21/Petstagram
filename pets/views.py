from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from pets.models import Pet


def add_pet(request: HttpRequest) -> HttpResponse:
    form = PetCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('accounts:profile_details', pk=1)

    context = {
        'form': form
    }

    return render(request, 'pets/pet-add-page.html', context)


def delete_pet(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    pet = get_object_or_404(Pet, slug=pet_slug)
    form = PetDeleteForm(request.POST or None, instance=pet)
    if request.method == 'POST':
        pet.delete()
        return redirect('pets:pet_details', slug=pet_slug)
    context = {
        'pet': pet,
        'form': form
    }
    return render(request, 'pets/pet-delete-page.html', context)


def pet_details(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    pet = Pet.objects.prefetch_related('photo_set').get(slug=pet_slug)
    context = {
        'pet': pet
    }
    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    pet = get_object_or_404(Pet, slug=pet_slug)
    form = PetEditForm(request.POST or None, instance=pet)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save()
            return redirect('common:home_page', slug=instance.slug)
    context = {
        'pet': pet,
        'form': form
    }
    return render(request, 'pets/pet-edit-page.html', context)