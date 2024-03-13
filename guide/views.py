from django.shortcuts import render
from .api import critical
from django.contrib.messages import constants as messages_constants
from .models import BankDetails
from .helpers import decrypt_data
# Create your views here.

MESSAGE_LEVEL = messages_constants.DEBUG
def message(request):
    
    
    critical(request,
             "A serious error occurred.")
    return render(request, "message.html")


def bank_details(request):

    user_bank_details = BankDetails.objects.get(
        user = request.user
    )
    account_number = decrypt_data.account_number(
        user_bank_details.account_number
    )
    
    context = {"account_number": account_number}
    return render(request, "bank_details.html",context)
    
    