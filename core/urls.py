from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/add/', views.ticket_add, name='ticket_add'),
    path('tickets/<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('tickets/<int:pk>/edit/', views.ticket_edit, name='ticket_edit'),
    path('tickets/<int:pk>/delete/', views.ticket_delete, name='ticket_delete'),
]
