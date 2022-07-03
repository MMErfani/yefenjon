"""yefenjon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from azbankgateways.urls import az_bank_gateways_urls
from peyment.views import go_to_gateway_view, callback_gateway_view
from django.contrib.auth import views
from account.views import Register, activate
admin.autodiscover()
urlpatterns = [
    path('', include('donate.urls')),
    path('', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path('activate/<uidb64>/<token>/',activate, name='activate'),
    path('admin/', admin.site.urls),
    path('bankgateways/', az_bank_gateways_urls()),
    path('go-to-gateway/<str:donate_to>/<int:amount>/', go_to_gateway_view),
    path('callback-gateway/<str:donate_to>/<int:amount>/', callback_gateway_view),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

