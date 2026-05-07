from django.urls import path, include

from pets.views import AddPetView, DeletePetView, PetDetailsView, EditPetView

app_name = 'pets'
urlpatterns = [
    path('add/', AddPetView.as_view(), name='add_pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', PetDetailsView.as_view(), name='pet_details'),
        path('edit/', EditPetView.as_view(), name='edit_pet'),
        path('delete/', DeletePetView.as_view(), name='delete_pet')
    ]))
]