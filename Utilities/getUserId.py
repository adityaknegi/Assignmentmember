from usertracker.models import User


def getUserId(user_email):
    try:
        user_data = User.objects.get(user_email=user_email)
    except User.DoesNotExist:
        user_data = None
    return user_data
