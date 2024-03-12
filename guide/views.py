from django.shortcuts import render
from .api import critical
from django.contrib.messages import constants as messages_constants
# Create your views here.

MESSAGE_LEVEL = messages_constants.DEBUG
def message(request):
    
    
    critical(request,
             "A serious error occurred.")
    return render(request, "message.html")