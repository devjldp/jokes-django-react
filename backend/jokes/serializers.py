# Importing the serializers module from Django REST framework
from rest_framework import serializers

# Importing the Joke model from the local models module
from .models import Joke


# Serializer for the Joke model
class JokeSerializer(serializers.ModelSerializer):
    # Meta class to define model and fields
    class Meta:
        # The model that this serializer works with
        model = Joke

        # Fields to include in the serialized representation
        fields = ["id", "joke", "category"]
