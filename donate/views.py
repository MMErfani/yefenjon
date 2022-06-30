from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from account.models import User

# Create your views here.
def index(request):
    context = {}
   
    return render(request, 'donate/index.html', context)


def donatePage(request, prof_id):
    context = {
       'page' : get_object_or_404(User, prof_id=prof_id)
    }
    
    
    return render(request, 'donate/donate.html', context)
