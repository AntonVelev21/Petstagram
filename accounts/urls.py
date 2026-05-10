from django.urls import path, include
from accounts.views import edit_profile, delete_profile, UserRegisterView, UserLoginView, \
    UserLogOutView, ProfileDetailsView

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile_details'),
        path('edit/', edit_profile, name='edit_profile'),
        path('delete/', delete_profile, name='delete_profile')
    ])),

    ]