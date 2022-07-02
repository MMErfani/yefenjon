from django import forms
from .models import donate

class DonateForm(forms.Form):
	class Meta:
		model = donate
		fields = ['name', 'description','amount','donate_to']
		
