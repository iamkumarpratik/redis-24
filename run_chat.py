from temp_chat_server import log, store_message
from argparse import ArgumentParser

parser = ArgumentParser(description='Text Chat Application')
parser.add_argument('username', type=str, help='Enter your username')
args = parser.parse_args()
print("You are logged in as", args.username)


def start_chatting():
    '''This function starts the chat.
    '''
    try:
        while True:
            input_message = str(input("---->"))
            store_message(args.username, input_message)
    except KeyboardInterrupt:
        log.info("Exiting the chat.")


if __name__ == "__main__":
    start_chatting()
