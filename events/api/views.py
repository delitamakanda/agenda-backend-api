from rest_framework import generics, permissions
from ..models import Event, EventGuest, Contact, UserInfo, Circle, Invitation
from .serializers import EventSerializer, EventGuestSerializer, ContactSerializer, CircleSerializer, InvitationSerializer, UserInfoSerializer

from authentication.api.permissions import AnonPermissionOnly, IsOwnerOrReadOnly

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.AllowAny,)


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.AllowAny,)


class EventGuestListView(generics.ListAPIView):
    queryset = EventGuest.objects.all()
    serializer_class = EventGuestSerializer
    permission_classes = (permissions.AllowAny,)


class EventGuestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventGuest.objects.all()
    serializer_class = EventGuestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
