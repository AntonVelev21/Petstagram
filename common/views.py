from django.contrib import messages
from django.db.models import Exists, OuterRef, Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView
from pyperclip import copy

from common.forms import CommentForm, SearchForm
from common.models import Like
from photos.models import Photo



class IndexView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 2

    def get_queryset(self):
        pet_name = self.request.GET.get('pet_name')
        photo = Photo.objects.prefetch_related('tagged_pets').annotate(likes_count=Count('likes'))

        if pet_name:
            photo = (Photo.objects.prefetch_related('tagged_pets').
                    filter(tagged_pets__name__icontains=pet_name)).annotate(likes_count=Count('likes'))

        if self.request.user.is_authenticated:
            photo = photo.annotate(is_liked_by_user=(Exists(Like.objects.filter(to_photo=OuterRef('pk'),
                                                                                user=self.request.user))))
        return photo


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['form'] = SearchForm(self.request.GET)
        context['all_photos'] = context['page_obj']
        return context
"""
To do!
Make photos show red heart when liked by the current user and withe when don't
 (Try do it in template and then in the Index and Photo detail views)
"""



def like_view(request: HttpRequest, photo_id) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        like = Like.objects.filter(to_photo=photo_id).last()
        if like and like.user == user:
            like.delete()
        else:
            Like.objects.create(
                to_photo_id=photo_id,
                user=user
            )

        return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")

    return redirect('accounts:login')



def share_view(request: HttpRequest, photo_id) -> HttpResponse:
    copy(request.META['HTTP_REFERER'][:-1] + resolve_url('photos:photo_details', photo_id))
    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")



def add_comment(request: HttpRequest, photo_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            photo = Photo.objects.get(id=photo_id)
            form = CommentForm(request.POST or None)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.photo = photo
                comment.user_id = request.user.id
                form.save()
            print(form.errors)

            return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")

    return redirect('accounts:login')

