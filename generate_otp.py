from config import REDIS
from random import randint


def generate_otp_number() -> int:
    '''This function generates a random number
    return:
        int: A random number between 0 and 999999
    '''
    return randint(0, 999999)


def generate_secret_code(username: str, expiry_time: int) -> dict:
    '''This function generates a secret code which 
    will have an expiry time of passed by the user.
    Parameters:
        username: str: The username of the user
        expiry_time: int: The expiry time of the OTP
    return:
        dict: A dictionary containing the message and success key
    '''
    code: int = generate_otp_number()
    REDIS.set(username, code, ex=expiry_time)
    return {"message": f"OTP has been generated for {username}. It is {code}. It will expire in {expiry_time} seconds.", "success": True}
