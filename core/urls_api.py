from django.urls import path
from . import api_views

urlpatterns = [
    path('api/tickets/', api_views.ticket_list_api, name='ticket_list_api'),
]
