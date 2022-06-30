from django.db import models
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.
class User(AbstractUser):
	card_number = models.IntegerField(verbose_name="شماره حساب", default=0)
	avatar = models.ImageField(upload_to="avatars",verbose_name="آواتار", default='NULL')
	job = models.CharField(max_length=250, verbose_name="شغل / حرفه", default="")

	
