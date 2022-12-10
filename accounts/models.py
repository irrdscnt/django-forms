from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone=models.CharField(blank=True,null=True,max_length=100)
    USER_TYPE = (
        ('Администратор', 'Администратор'),
        ('Пользователь','Пользователь'),
    )
    user_type = models.CharField(choices=USER_TYPE,max_length=100)
    if USER_TYPE[0][0]=="Администратор":
        is_admin = models.BooleanField(default=True)
    elif USER_TYPE[0][0]== "Пользователь":
        is_admin = models.BooleanField(default=False)

