from django.urls import path
from . import views

# jwt 토큰 발급용
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('signup/', views.signup),
    # 토큰 발급용 url
    path('api-token-auth/', obtain_jwt_token),
]