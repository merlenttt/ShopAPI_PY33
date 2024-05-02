from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_lenght=4, required=True, wirte_only=True)
    password_confirm = serializers.CharField(min_lenght=4, required=True, write_only=True)

    class Meta:
        model = User
        fields = 'email', 'password', 'password_confirm'

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password_confirm')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпали!')
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user