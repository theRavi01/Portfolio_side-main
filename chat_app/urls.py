from django.urls import path
from . import views




urlpatterns = [
path('',views.home,name='home'),
 path('contact/', views.contact_view, name='contact'),
 path('contact_success/', views.contact_success, name='contact_success'),
    
]
