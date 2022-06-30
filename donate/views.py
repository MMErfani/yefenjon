from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from account.models import User

# Create your views here.
def index(request):
    context = {}
   
    return render(request, 'donate/index.html', context)


def donatePage(request, username):
    context = {
       'info' : get_object_or_404(User, username=username)
    }
    
    
    return render(request, 'donate/donate.html', context)
