from config import REDIS
from random import randint


def generate_otp_number():
    '''This function generates a random number'''
    return randint(0, 999999)


def generate_secret_code(username: str, expiry_time: int):
    '''This function generates a secret code which 
    will have an expiry time of passed by the user'''
    code = generate_otp_number()
    REDIS.set(username, code, ex=expiry_time)
    return {"message": f"OTP has been generated for {username}. It is {code}. It will expire in {expiry_time} seconds.", "success": True}
