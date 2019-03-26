import unittest
from src.model import PasswordManager
from src.config import *


class PasswordManagerTest(unittest.TestCase):
    # create instance of PasswordManager, assign username & password
    def setUp(self):
        username = 'hello'
        password = '123qweA$'
        self.manager = PasswordManager.get_instance()
        self.manager.set_user_name(username)
        self.manager.set_password(password)

    # Return True if the password you entered is matched with the password's PasswordManager
    def test_verify_password_true(self):
        password_input = '123qweA$'
        result = self.manager.verify_password(password_input)
        self.assertTrue(result)

    # Return False because the password you entered is not matched with the password's PasswordManager
    def test_verify_password_false(self):
        password_input = 'hello'
        result = self.manager.verify_password(password_input)
        self.assertFalse(result)

    # Return True if the password you entered is following the list rules
    def test_validate_password_true(self):
        password_input = 'Hello1!'
        is_valid, msg = self.manager.validate_password(password_input)
        self.assertTrue(is_valid)
        self.assertEqual(msg, 'valid')

    # Return False because the password contain whitespace
    def test_validate_password_contain_space(self):
        password_input = 'He llo'
        is_valid, msg = self.manager.validate_password(password_input)
        self.assertFalse(is_valid)
        self.assertEqual(msg, MSG_PASSWORD_CONTAIN_SPACE)

        password_input2 = ' Hello2'
        is_valid, msg = self.manager.validate_password(password_input2)
        self.assertFalse(is_valid)

        password_input3 = 'Hello3   '
        is_valid, msg = self.manager.validate_password(password_input3)
        self.assertFalse(is_valid)

    # Return False because the password is less than 6 characters
    def test_validate_password_minimum_length(self):
        password_input = 'Ha1#'
        is_valid, msg = self.manager.validate_password(password_input)
        self.assertFalse(is_valid)
        self.assertEqual(msg, MSG_PASSWORD_MINIMUM_LENGTH)

    # Return False because the password missing uppercase or lowercase or both type of letter
    def test_validate_password_missing_uppercase_lowercase(self):
        missing_letter = '123123!'
        is_valid, msg = self.manager.validate_password(missing_letter)
        self.assertFalse(is_valid)
        self.assertEqual(msg, MSG_PASSWORD_CONTAIN_LOWER_AND_UPPER)

        missing_lowercase = '123ABC!'
        is_valid, msg = self.manager.validate_password(missing_lowercase)
        self.assertFalse(is_valid)
        self.assertEqual(msg, MSG_PASSWORD_CONTAIN_LOWER_AND_UPPER)

        missing_uppercase = '123abc!'
        is_valid, msg = self.manager.validate_password(missing_uppercase)
        self.assertFalse(is_valid)
        self.assertEqual(msg, MSG_PASSWORD_CONTAIN_LOWER_AND_UPPER)

    # Return False because the password missing digit or symbol or both type
    def test_validate_password_missing_digit_symbol(self):
        missing_digit_and_symbol = 'abcABC'
        is_valid, msg = self.manager.validate_password(missing_digit_and_symbol)
        self.assertFalse(is_valid)
        self.assertEqual(msg, MSG_PASSWORD_CONTAIN_DIGIT_AND_SYMBOL)

        missing_digit = 'abcABC!!'
        is_valid, msg = self.manager.validate_password(missing_digit)
        self.assertFalse(is_valid)
        self.assertEqual(msg, MSG_PASSWORD_CONTAIN_DIGIT_AND_SYMBOL)

        missing_symbol = 'abcABC123'
        is_valid, msg = self.manager.validate_password(missing_symbol)
        self.assertFalse(is_valid)
        self.assertEqual(msg, MSG_PASSWORD_CONTAIN_DIGIT_AND_SYMBOL)

    # Return True if the new password matched the rules
    def test_change_password_true(self):
        new_password = 'abcABC123@!#'
        is_valid, msg = self.manager.set_new_password(new_password)
        is_success = self.manager.verify_password(new_password)
        self.assertTrue(is_valid)
        self.assertEqual(msg, 'valid')
        self.assertTrue(is_success)


if __name__ == '__main__':
    unittest.main()