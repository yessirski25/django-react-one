from django.shortcuts import render
from django.db import IntegrityError
from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import *
from .serializers import *

# Create your views here.
class ContactView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CreateContact(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        ##used *args and **kwargs to override the original post method of CreateAPIView
        try:
            return super().post(request, *args, **kwargs)
        except IntegrityError:
            return Response({"detail": "A contact with this number already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteContact(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def delete(self, request, *args, **kwargs):
        try:
            contact = self.get_object()
            contact.delete()
            return Response({"detail": "Contact deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({"detail": "Contact not found."}, status=status.HTTP_404_NOT_FOUND)

class UpdateContact(generics.UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def put(self, request, *args, **kwargs):        
        try:
            contact = Contact.objects.all()
            serializer = self.get_serializer(contact, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({"detail": "Contact updated successfully."}, status=status.HTTP_200_OK)
        except Http404:
            return Response({"detail": "Contact not found."}, status=status.HTTP_404_NOT_FOUND)
        