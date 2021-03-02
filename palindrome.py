from typing import Union


def _convert_to_string(subject: any) -> str:
    subject_type = type(subject)
    if subject_type == int or subject_type == float:
        return str(subject).replace('.', '')
    raise TypeError('%s is not a supported type' % type(subject))


def _verify_str_is_palindrome(subject: str) -> bool:
    if len(subject) < 2:
        return False
    return subject[::-1] == subject


def _normalize_str(string: str) -> str:
    return string.lower().strip()


def is_palindrome(subject: Union[str, float, int]) -> bool:
    if type(subject) != str:
        subject = _convert_to_string(subject)
    subject = _normalize_str(subject)
    return _verify_str_is_palindrome(subject)
