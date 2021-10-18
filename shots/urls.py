from django.urls import path

from .views import ShotListView, shot_detail


urlpatterns = [
    path(
        'projects/<str:project_code>/shots/',
        ShotListView.as_view(),
        name='shot-list'
    ),
    path(
        'projects/<str:project_code>/shots/<str:shot_title>',
        shot_detail,
        name='shot-detail'
    ),
]
