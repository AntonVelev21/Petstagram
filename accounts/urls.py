from django.urls import path, include
from accounts.views import register, login, profile_details, edit_profile, delete_profile

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/<int:pk>/', include([
        path('', profile_details, name='profile_details'),
        path('edit/', edit_profile, name='edit_profile'),
        path('delete/', delete_profile, name='delete_profile')
    ])),

    ]