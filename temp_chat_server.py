from config import REDIS
from threading import Thread
import logging as log


log.basicConfig(level=log.INFO)


def store_message(username, message: str) -> dict:
    '''This function stores the message in the Redis database.
    Parameters:
        message: str: The message to be stored
    return:
        dict: A dictionary containing the message and success key.
    '''
    res = REDIS.publish('current_channel', f"{username}: {message}")
    return res


def get_message(username: str) -> dict:
    '''This function retrieves the message from the Redis database.
    Parameters:
        username: str: The username of the user
    return:
        dict: A dictionary containing the message and success key.
    '''
    message = REDIS.lrange(username, 0, -1)
    if message:
        return {"message": f"Message for {username} is {message}.", "success": True}
    return {"message": f"No message found for {username}.", "success": False}


def clear_chat(username: str) -> dict:
    '''This function clears the chat for the user.
    Parameters:
        username: str: The username of the user
    return:
        dict: A dictionary containing the message and success key.
    '''
    REDIS.delete(username)
    return {"message": f"Chat has been cleared for {username}.", "success": True}


def msg_listener():
    pub_sub = REDIS.pubsub()
    pub_sub.subscribe('current_channel')
    for msg in pub_sub.listen():
        log.info(msg.get('data'))


if __name__ == "__main__":
    try:
        Thread(target=msg_listener).start()
        log.info("A separate thread has been started to listen to the messages.")
        log.info("You can start sending messages.")
    except KeyboardInterrupt:
        log.info("Exiting the chat application.")
