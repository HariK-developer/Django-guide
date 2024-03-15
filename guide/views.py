from django.shortcuts import render
from django.contrib.messages import constants as messages_constants
from .api import critical
from .models import BankDetails, Book
from .helpers import decrypt_data

# Create your views here.

MESSAGE_LEVEL = messages_constants.DEBUG

def fake_data():
    """
    Generate fake data for the database.

    Args:
        None

    Returns:
        None

    """
    x = Book(title='Book3',author_id=3)
    x.save()
    
# fake_data()


# books = Book.objects.prefetch_related('author').all()

# for book in books:
#     print(book.title, book.author.name)


def message(request):
    """
    This function logs a critical error message to the user's session.

    Parameters:
        request (HttpRequest): The incoming request object.
        message (str): The error message to be logged.

    Returns:
        HttpResponse: An empty response with a status code of 200.
    """
    critical(request, "A serious error occurred.")
    return render(request, "message.html")


def bank_details(request):
    """
    This function retrieves the bank details of the currently logged in user.

    Parameters:
        request (HttpRequest): The incoming request object.

    Returns:
        HttpResponse: The response object containing the bank details.
    """
    user_bank_details = BankDetails.objects.get(user=request.user)
    account_number = decrypt_data.account_number(user_bank_details.account_number)

    context = {"account_number": account_number}
    return render(request, "bank_details.html", context)



