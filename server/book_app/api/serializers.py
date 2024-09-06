from rest_framework import serializers
from .models import *

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def validate_contactNo(self, value):
        if self.instance and self.instance.contactNumber == value:
            return value

        if Contact.objects.filter(contactNumber = value).exists():
            raise serializers.ValidationError("A contact with this number already exists")
        return value
    
    def update(self, instance, validated_data):
        # For partial updates, only update fields provided in `validated_data`
        for attr, value in validated_data.items():
            if value != "":
                setattr(instance, attr, value)
        instance.save()
        return instance