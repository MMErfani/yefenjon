from django.urls import path

from . import views

app_name = "donate"
urlpatterns = [
    path('', views.index, name='home'),
    path('donate/<slug:slug>', views.donatePage, name="donatePage")
]
