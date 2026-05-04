from django.urls import path, include

from pets.views import add_pet, pet_details, edit_pet, delete_pet

app_name = 'pets'
urlpatterns = [
    path('add/', add_pet, name='add_pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', pet_details, name='pet_details'),
        path('edit/', edit_pet, name='edit_pet'),
        path('delete/', delete_pet, name='delete_pet')
    ]))
]