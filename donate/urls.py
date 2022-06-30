from django.urls import path

from . import views

app_name = "donate"
urlpatterns = [
    path('', views.index, name='home'),
    path('donate/<slug:username>', views.donatePage, name="donatePage")
]
# urlpatterns += patterns('',(r'^donate/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT}))
