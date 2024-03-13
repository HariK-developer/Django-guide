

from django.urls import path
from .views import message,bank_details
from .api import api


urlpatterns = [
    path('messages/',message,name='messages'),
    path('bank-details/',bank_details,name='bank-details'),
    path("api/",api.urls)
]