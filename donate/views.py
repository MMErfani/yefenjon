from django.shortcuts import render, get_object_or_404
from django.shortcuts import render

# Create your views here.
def index(request):
	context = {}
   
	return render(request, 'donate/index.html', context)


def donatePage(request, int):
	
	
	return render(request, 'donate/donate.html')
