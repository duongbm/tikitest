from src.model import PasswordManager
from src.storage import read_data
from src.config import *


class Menu:
    def __init__(self):
        self.manager = PasswordManager.get_instance()
        data = read_data()
        if data:
            self.manager.set_user_name(data[USER_NAME])
            self.manager.set_password(data[PASSWORD])

    def new_user(self):
        username = input(MSG_INPUT_USER_NAME)
        password = input(MSG_INPUT_PASSWORD)
        self.manager.set_user_name(username)
        self.manager.set_password(password)
        self.manager.save()
        print(MSG_CREATED_SUCCESS_USER_PASSWORD)

    def validate_password(self):
        while True:
            password = input(MSG_INPUT_PASSWORD)
            valid, msg = self.manager.validate_password(password)
            if not valid:
                print(f'=> {msg}')
            else:
                print(MSG_PASSWORD_IS_VALID)
                break

    def login(self):
        if not hasattr(self.manager, PASSWORD):
            print(MSG_MUST_CREATE_USER_PASSWORD)
        else:
            password = input(MSG_INPUT_PASSWORD)
            result = self.manager.verify_password(password)
            if result == False:
                print(MSG_WRONG_PASSWORD)
            else:
                print(MSG_LOGIN_SUCCESS)

    def change_password(self):
        if not hasattr(self.manager, PASSWORD):
            print(MSG_MUST_CREATE_USER_PASSWORD)
        else:
            new_password = input(MSG_INPUT_PASSWORD)
            is_changed, msg = self.manager.set_new_password(new_password)
            if is_changed:
                print(MSG_CHANGE_PASSWORD_SUCCESS)
            else:
                print(f'=> {msg}')

    def print_dash(self):
        print('--------------------')

    def print(self):
        self.print_dash()
        print('Choose the number')
        self.print_dash()
        print(MODE_NEW_USER)
        print(MODE_VALIDATE_PASSWORD)
        print(MODE_LOGIN)
        print(MODE_CHANGE_PASSWORD)
        print(MODE_QUIT)
        self.print_dash()