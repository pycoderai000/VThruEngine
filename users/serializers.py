from django.http import JsonResponse

from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

from users.models import CustomUser
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id',"email","name","image","phone_number","verified","receive_updates_on_notifications","receive_updates_on_email","receive_updates_on_sms","receive_offers_on_notifications","receive_offers_on_email","receive_offers_on_sms","cart"]




class RegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=250, required=False)
    phone_number = serializers.CharField(max_length=250, required=False)

    def get_cleaned_data(self):
        super(RegisterSerializer, self).get_cleaned_data()
        return {
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'name': self.validated_data.get('name', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.phone_number = self.validated_data.get('phone_number', '')
        user.name = self.validated_data.get('name', '')
        user.save()
        return user