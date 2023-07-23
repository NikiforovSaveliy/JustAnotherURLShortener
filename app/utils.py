from random import choice

import validators


def generate_slug(length=7) -> str:
    url_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U',
                   'V', 'W', 'X', 'Y', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                   'q',
                   'r', 's', 't', 'u', 'v', 'w', 'x', 'y', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '_', '-']

    return ''.join(choice(url_letters) for i in range(length))


def validate_url(url: str) -> bool:
    try:
        return validators.url(url)
    except validators.ValidationFailure:
        return False
