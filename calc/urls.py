from django.urls import path
from . import views
urlpatterns= [
    path('index.html', views.home, name='home'),
    path('contact.html',views.contact,name='contact')
]