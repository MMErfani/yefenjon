from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView

# Create your views here.
    
class Profile(LoginRequiredMixin, UpdateView):
	model = User
	fields = ['first_name', 'last_name', 'username', 'email', 'card_number','avatar','job']
	template_name = 'registration/home.html'
	success_url = reverse_lazy('account:Profile')
	
	def get_object(self):
		return User.objects.get(pk = self.request.user.pk)
