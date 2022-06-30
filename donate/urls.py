from django.urls import path

from . import views

app_name = "donate"
urlpatterns = [
    path('', views.index, name='home'),
    path('donate/<int:pk>', views.donatePage, name="donatePage")
]
