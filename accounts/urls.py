from django.urls import path, include
from accounts.views import ProfileEditView, ProfileDeleteView, UserRegisterView, UserLoginView, \
    UserLogOutView, ProfileDetailsView

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile_details'),
        path('edit/', ProfileEditView.as_view(), name='edit_profile'),
        path('delete/', ProfileDeleteView.as_view(), name='delete_profile')
    ])),

    ]