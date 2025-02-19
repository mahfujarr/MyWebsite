from django.urls import path
from Home.views import *

urlpatterns = [
    path('', home, name='home'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('resume/', resume, name='resume'),
]