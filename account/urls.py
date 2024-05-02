from django.urls. import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . views import RegisterView, ActivateView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/,Ac')
]
