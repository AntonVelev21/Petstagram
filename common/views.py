from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from common.forms import CommentForm, SearchForm
from common.models import Like
from photos.models import Photo


def index(request: HttpRequest) -> HttpResponse:
    photos = Photo.objects.prefetch_related('tagged_pets', 'likes')
    form = SearchForm(request.GET)
    if form.is_valid():
        pet_name = form.cleaned_data['pet_name']
        photos = Photo.objects.prefetch_related('tagged_pets', 'likes').filter(tagged_pets__name__icontains=pet_name)
    context = {
        'all_photos': photos,
        'comment_form': CommentForm,
        'form': form
    }
    return render(request, 'common/home-page.html', context)



def like_view(request: HttpRequest, photo_id) -> HttpResponse:
    like = Like.objects.filter(to_photo=photo_id).first()
    if like:
        like.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_id
        )

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")



def share_view(request: HttpRequest, photo_id) -> HttpResponse:
    copy(request.META['HTTP_REFERER'][:-1] + resolve_url('photos:photo_details', photo_id))
    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")



def add_comment(request: HttpRequest, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.photo = photo
            form.save()
        print(form.errors)

        return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")

