import random
import string


def generate_user_hash():
    hash_length = 50
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(hash_length)))



