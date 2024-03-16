from django.contrib.messages import add_message
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
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
    return {
        "message": "Hello World",
        "session": request.session.get("sessionid", "no value"),
    }


@api.get("/user/")
def user(request):

    try:
        # user = User.objects.get(id=1)
        # user = User.objects.get_or_create(username="haridev",password=make_password("123456"))
        # user = User.objects.bulk_create(
        #     [
        #         User(username="xyz", password=make_password("123456")),
        #         User(username="abc", password=make_password("123456")),
        #     ]
        # )
        user = User.objects.all()
        return {"name": user.count()}
    except Exception as e:
        return {"error": str(e)}
