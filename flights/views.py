from .models import Flight, Booking
from .serializers import FlightSerializer, BookingsSerializer
from rest_framework.generics import ListAPIView
from datetime import date

class FlightsView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class BookingView(ListAPIView):
	queryset = Booking.objects.filter(date__gt=date.today())
	serializer_class= BookingsSerializer

		


