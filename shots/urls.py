from django.urls import path

from .views import ShotListView


urlpatterns = [
    path(
        'projects/<str:project_code>/shots/',
        ShotListView.as_view(),
        name='shot-list'
    ),
]
