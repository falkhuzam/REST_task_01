from rest_framework import serializers
from .models import Flight
from .models import Booking



class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'destination', 'time','price']

class BookingsSerializer(serializers.ModelSerializer):
	class Meta:
		model= Booking
		fields = ['flight','date', 'id']