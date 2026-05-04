from django.urls import path, include

from photos.views import add_photo, photo_details, edit_photo, delete_photo

app_name = 'photos'
urlpatterns = [
    path('add/', add_photo, name='add_photo'),
    path('<int:pk>/', include([
        path('', photo_details, name='photo_details'),
        path('edit/', edit_photo, name='edit_photo'),
        path('delete/', delete_photo, name='delete_photo')
    ]))
]