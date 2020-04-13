
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import generics, permissions, views
from rest_framework.response import Response
from rest_framework_jwt import settings

from authentication.api.permissions import AnonPermissionOnly
from authentication.api.serializers import UserRegisterSerializer, UserDetailSerializer, UserPublicSerializer

jwt_payload_handler             = settings.api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = settings.api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler    = settings.api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()

class AuthAPIView(views.APIView):
    permission_classes = (AnonPermissionOnly,)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return Response({'detail': 'You are already authenticated'}, status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        qs = User.objects.filter(
                Q(username__iexact=username)|
                Q(email__iexact=username)
            ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, request=request)
                return Response(response)
        return Response({"detail": "Invalid credentials"}, status=401)


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AnonPermissionOnly,)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def get_serializer_context(self):
        return {'request': self.request}
