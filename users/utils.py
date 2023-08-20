import random
import string


def login_code_generator():
    chars = string.digits
    return ''.join(random.choice(chars) for _ in range(4))


def referral_code_generator():
    chars = string.digits + string.ascii_uppercase
    return ''.join(random.choice(chars) for _ in range(6))
