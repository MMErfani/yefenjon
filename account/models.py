from django.db import models
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.
class User(AbstractUser):
	prof_id = models.SlugField(max_length=200,verbose_name="آیدی",default="NULL")
	card_number = models.IntegerField(verbose_name="شماره حساب", default=0)
	avatar = models.ImageField(upload_to="avatars",verbose_name="آواتار", default='NULL')
	

	
