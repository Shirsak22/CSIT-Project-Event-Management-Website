from django.urls import path
from .views import index,events,booking,contact,about,login,signup


urlpatterns = [
    path('',index, name='index'),
    path('events/',events, name='events'),
    path('booking/',booking, name='booking'),
    path('contact/',contact, name='contact'),
    path('about/',about, name='about'),
    path('login/',login, name='login'),
    path('signup/',signup, name='signup'),
]
