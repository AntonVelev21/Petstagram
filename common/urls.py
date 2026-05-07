from django.urls import path

from common.views import like_view, share_view, add_comment, IndexView

app_name = 'common'
urlpatterns = [
    path('', IndexView.as_view(), name='home_page'),
    path('like/<int:photo_id>/', like_view, name='like'),
    path('share/<int:photo_id>/', share_view, name='share'),
    path('comment/<int:photo_id>/', add_comment, name='add-comment')
]