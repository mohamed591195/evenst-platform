from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):

    owner = serializers.CharField(source='owner.email', read_only=True)
    
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'owner', 'date', 'participants', 'participants_count']