from django.db import models
from django.contrib.auth.models import AbstractUser

# 유저 모델 커스터마이징을 위한 AbstractUser 상속
class User(AbstractUser):
    pass