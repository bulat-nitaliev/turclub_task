from rest_framework import serializers
from .models import Trip, Application
from django.core.validators import FileExtensionValidator

class TripSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    class Meta:
        model = Trip
        fields = '__all__'
        extra_kwargs = {
            'photo': {'required': True}
        }



class ApplicationSerializer(serializers.ModelSerializer):
    trip_title = serializers.SerializerMethodField()
    
    class Meta:
        model = Application
        fields = ['id', 'full_name', 'email', 'phone', 'is_canceled', 'created_at', 'trip_title']
        
    def get_trip_title(self, obj):
        return obj.trip.title if obj.trip else None