from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User
from django.views.generic import UpdateView

# Create your views here.

@login_required
def home(request):
    context = {}
    return render(request, 'registration/home.html',context)
    
class EditProfile(UpdateView):
	model = User
	fields = ['first_name', 'last_name', 'username', 'email', 'card_number','avatar','job']
	template_name = 'registration/edit-profile.html'
	
	def get_object(self):
		return User.objects.get(pk = self.request.user.pk)
