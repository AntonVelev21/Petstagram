from django.core.exceptions import PermissionDenied
from django.db.models import Exists, OuterRef, Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from common.models import Like
from photos.forms import PhotoCreateForm, PhotoEditForm
from photos.models import Photo


def add_photo(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user_id = request.user.id
            photo.save()
            return redirect('common:home_page')
    context = {
        'form': form
    }
    return render(request, 'photos/photo-add-page.html', context)


def photo_details(request: HttpRequest, pk: int) -> HttpResponse:
    photo = Photo.objects.annotate(likes_count=Count('likes')).get(pk=pk)
    if request.user.is_authenticated:
        photo = Photo.objects.annotate(likes_count=Count('likes'),
                                       is_liked_by_user=(Exists(Like.objects.filter(to_photo=OuterRef('pk'),
                                       user=request.user)))).get(pk=pk)
    context = {
        'photo': photo
    }
    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request: HttpRequest, pk: int) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    photo = get_object_or_404(Photo, pk=pk)
    if photo.user != request.user:
        raise PermissionDenied()
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
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    photo = Photo.objects.get(pk=pk)
    if photo.user != request.user:
        raise PermissionDenied()
    photo.delete()
    return redirect('common:home_page')
