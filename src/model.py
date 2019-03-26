import hashlib
from src.storage import write
from src.util import *
from src.config import *


class PasswordManager:
    __instance = None

    @staticmethod
    def get_instance():
        if PasswordManager.__instance == None:
            PasswordManager()
        return PasswordManager.__instance

    def __init__(self):
        if PasswordManager.__instance != None:
            raise Exception('Can\'t instance the class. Use get_instance() instead')
        else:
            PasswordManager.__instance = self

    def encrypt(self, plain_password):
        """
        :param plain_password: a plain text password entered
        :return: a encrypted password(algorithm sha512)
        """
        return hashlib.sha512(plain_password.encode()).hexdigest()

    def verify_password(self, password):
        """
        :param password: a password entered
        :return:
            - True if the password is matched password's PasswordManager
            - Else False
        """
        return True if self.encrypt(password) == self.password else False

    def set_new_password(self, new_password):
        """
        :param new_password: a new password entered
        :return:
            - True if the new password is valid and save to file
            - False if password isn't matched the rules
        """
        is_valid, msg = self.validate_password(new_password)
        if is_valid:
            self.set_password(new_password)
            self.save()
            return True, msg
        else:
            return False, msg

    def validate_password(self, password):
        """
        :param password: a password entered
        :return:
            - True if the password not contain space & greater than 6 character &
                        contain at least a lowercase, a uppercase, a digit, a symbol
            - False if the password is missed the rule
        """
        if is_contain_space(password):
            return False, MSG_PASSWORD_CONTAIN_SPACE
        elif not is_minimum_length(password):
            return False, MSG_PASSWORD_MINIMUM_LENGTH
        elif not is_contain_lower_and_upper(password):
            return False, MSG_PASSWORD_CONTAIN_LOWER_AND_UPPER
        elif not is_contain_digit_and_symbol(password):
            return False, MSG_PASSWORD_CONTAIN_DIGIT_AND_SYMBOL
        else:
            return True, 'valid'

    def save(self):
        """
        save username & password to password.txt file
        """
        data = {USER_NAME: self.username, PASSWORD: self.password}
        write(data)

    def get_user_name(self):
        return self.username

    def set_user_name(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, plain_password):
        self.password = self.encrypt(plain_password)