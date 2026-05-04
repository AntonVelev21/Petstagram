from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from photos.forms import PhotoCreateForm, PhotoEditForm
from photos.models import Photo


def add_photo(request: HttpRequest) -> HttpResponse:
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('common:home_page')
    context = {
        'form': form
    }
    return render(request, 'photos/photo-add-page.html', context)


def photo_details(request: HttpRequest, pk: int) -> HttpResponse:
    photo = Photo.objects.prefetch_related('likes', 'comments').get(pk=pk)
    context = {
        'photo': photo
    }
    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request: HttpRequest, pk: int) -> HttpResponse:
    photo = get_object_or_404(Photo, pk=pk)
    form = PhotoEditForm(request.POST or None, request.FILES or None, instance=photo)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('common:home_page')
    context = {
        'form': form,
    }
    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request: HttpRequest, pk: int) -> HttpResponse:
    Photo.objects.get(pk=pk).delete()
    return redirect('common:home_page')
