from django.contrib.auth.models import User

from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_null=False, allow_blank=False, source='username')
    password = serializers.CharField(write_only=True, max_length=128)

    class Meta:
        model = User
        fields = (
            'name',
            'email',
            'password',
        )


class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data.pop('refresh')
        data.pop('access')
        data['token'] = f'Bearer {str(refresh.access_token)}'
        data['success'] = True

        return data
