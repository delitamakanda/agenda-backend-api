from rest_framework import serializers
from ..models import Event, EventGuest, Circle, Contact, UserInfo, Invitation

class EventGuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventGuest
        fields = ('id', 'event', 'guest', 'status',)


class EventSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(format="%Y-%m-%d", source='date')
    guests = EventGuestSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'guests', 'start', 'location', 'color',)


class CircleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Circle
        fields = (
            'id',
            'name',
            'owner',
        )

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ('id', 'circle', 'notes',)

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = (
            'id',
            'owner',
            'user',
            'invitation_send',
            'invitation_accepted',
            'optional_informations',
        )

class InvitationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invitation
        fields = (
            'id',
            'email',
            'sender',
        )