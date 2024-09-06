from django.urls import path
from .views import *

urlpatterns = [
    path('contacts/', ContactView.as_view()),
    path('contacts/create/', CreateContact.as_view()),
    path('contacts/<int:pk>/delete/', DeleteContact.as_view()),
    path('contacts/<int:pk>/update/', UpdateContact.as_view()),
]