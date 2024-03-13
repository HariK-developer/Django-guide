from django.contrib.messages import add_message
from ninja import NinjaAPI
from . import constants


api = NinjaAPI()

def critical(request, message, extra_tags="", fail_silently=False):

    add_message(
        request,
        constants.CRITICAL,
        message,
        extra_tags=extra_tags,
        fail_silently=fail_silently,
    )


@api.get("/")
def add(request):
    return {"message":"Hello World"}

