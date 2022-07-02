from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from account.models import User
from .forms import DonateForm
from .models import donate
# Create your views here.
def index(request):
    context = {}
   
    return render(request, 'donate/index.html', context)


def donatePage(request, username):
    form = DonateForm(request.POST)
    context = {'info' : get_object_or_404(User, username=username),'form' : form}

    return render(request, 'donate/donate.html', context)
