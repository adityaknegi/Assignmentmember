from usertracker.models import User


def validate_user(user_email, user_hash):
    try:
        user_data = User.objects.get(user_email=user_email, user_hash=user_hash)
    except User.DoesNotExist:
        user_data = None
    return user_data
