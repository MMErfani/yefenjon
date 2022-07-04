from django.db import models
from account.models import User
from django.utils import timezone
# Create your models here.

class donate(models.Model):
	donate_id = models.AutoField(primary_key=True)
	amount = models.IntegerField(verbose_name="مبلغ", default=0)
	name = models.CharField(max_length=250, verbose_name="نام", default="ناشناس")
	description = models.TextField(max_length=2500, verbose_name="متن",default="")
	donate_to = models.CharField(max_length=250, verbose_name="پرداخت به")
	date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ و زمان")
	payment_status = models.BooleanField(default=False, verbose_name="وضعیت پرداخت")
	tracking_code = models.IntegerField(unique=True,verbose_name="کد پیگیری")
