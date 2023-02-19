from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from user.serializers import RegisterSerializer


class RegisterViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        raw_password = serializer.validated_data.pop('password')
        instance = serializer.save()
        instance.set_password(raw_password)
        instance.save()
        return instance
