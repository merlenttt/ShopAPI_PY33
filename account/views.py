
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .utils import send_activation_code
from drf_yasg.utils  import swagger_auto_schema

from .serializers import RegisterSerializer
User = get_user_model()

class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        data = request, data
        serializer = RegisterSerializer(dta=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Вы успешно зарегистрировались!')
        
class ActivateView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, code=activation_code).first()
        if not user:
            return Response('Пользователь не найдет')
        user.activationn_code = ''
        user.is_active = True
        user.save()
        return Response('Активировано')