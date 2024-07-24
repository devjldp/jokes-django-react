# Importing everything needed for defining views
from .models import Joke
from .serializers import JokeSerializer
from rest_framework import generics

# Create your views here.
# Class-based view for listing and creating jokes


class JokeListCreate(generics.ListCreateAPIView):
    # Define the queryset to be used for retrieving data
    queryset = Joke.objects.all()

    # Define the serializer class to be used for converting data
    serializer_class = JokeSerializer
