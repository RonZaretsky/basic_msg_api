from django.urls import path
from .views import *

urlpatterns = [
    path('messages/', Messages.as_view())
]