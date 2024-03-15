from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.messages import constants as messages_constants
from django.shortcuts import get_object_or_404
from django.db import transaction
from .api import critical
from .models import BankAccount, BankDetails, Book, Student
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
    x = Book(title="Book3", author_id=3)
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


"""Django Transaction Details"""


@transaction.atomic
def transfer_funds(request, from_account_number, to_account_number, amount):
    """
    This function debits an account and credits another account.

    Args:
        request (HttpRequest): The incoming request object.
        from_account_number (str): The account number of the source account.
        to_account_number (str): The account number of the destination account.
        amount (int): The amount to be transferred.

    Returns:
        JsonResponse: A JSON response containing a success or error message.

    Raises:
        ValueError: If the source or destination account does not exist.
        ValueError: If the source account does not have sufficient funds.

    """
    try:
        from_account = get_object_or_404(
            BankAccount, account_number=from_account_number
        )
        to_account = get_object_or_404(BankAccount, account_number=to_account_number)
        if from_account.balance < amount:
            return JsonResponse({"error": "Insufficient balance"}, status=400)

        from_account.balance -= amount
        from_account.save()

        to_account.balance += amount
        to_account.save()

        return JsonResponse({"message": "Transfer Successful"}, status=200)
    except Exception as e:

        return JsonResponse({"error": str(e)}, status=500)


"""Django Transaction other important concepts"""


@transaction.atomic
def my_transaction_function():
    """
    This function demonstrates the use of the Django transaction module.

    This function creates two Student objects, one with the name "David" and another with the name "John". If the creation of the second Student object fails, the transaction is rolled back, and an exception is raised.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the creation of the second Student object fails.

    """
    try:
        stu1 = Student.objects.create(name="David")
        # create a savepoint
        std = transaction.savepoint()

        stu2 = Student.objects.create(name="John")
        # Roll back to the savepoint
        transaction.savepoint_rollback(std)

    except Exception as e:
        # Roll back entire transaction in case of an exception
        transaction.set_rollback(True)


"""Django Transaction other important concepts 
    commit :- It makes all changes permanent to the database
"""


@transaction.atomic
def my_transaction_commit():
    """
    This function demonstrates the use of the Django transaction module.

    This function creates two Student objects, one with the name "David" and another with the name "John". If the creation of the second Student object fails, the transaction is rolled back, and an exception is raised.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the creation of the second Student object fails.

    """
    try:
        stu1 = Student.objects.create(name="David")

        # finalize the transaction by committing the changes
        transaction.commit()

    except Exception as e:
        # Roll back entire transaction in case of an exception
        transaction.set_rollback(True)


"""Django Transaction other important concepts 
    Nested Transactions :- Using context manager we can even implement nested transactions
"""


@transaction.atomic
def my_nested_transaction():
    """
    This function demonstrates the use of the Django transaction module.

    This function creates two Student objects, one with the name "David" and another with the name "John". If the creation of the second Student object fails, the transaction is rolled back, and an exception is raised.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If the creation of the second Student object fails.

    """
    stu1 = Student.objects.create(name="David")

    # finalize the transaction by committing the changes
    transaction.commit()

    with transaction.atomic():
        # perform nested transactions
        stu2 = Student.objects.create(name="John Doe")
   