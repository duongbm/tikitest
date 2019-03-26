import re
from src.config import MINIMUM_LENGTH


def is_contain_space(text):
    if re.search('\s+', text):
        return True
    return False


def is_minimum_length(text):
    if len(text) >= MINIMUM_LENGTH:
        return True
    return False


def is_contain_lower_and_upper(text):
    if re.search('[a-z]+', text):
        if re.search('[A-Z]+', text):
            return True
    return False


def is_contain_digit_and_symbol(text):
    if re.search('[0-9]+', text):
        if re.search('[\W_]+', text):
            return True
    return False