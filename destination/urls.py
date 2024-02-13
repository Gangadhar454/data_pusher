from django.urls import path
from destination.views import DestinationView

urlpatterns = [
    path('', DestinationView.as_view())
]