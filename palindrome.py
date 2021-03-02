from typing import Union


def _convert_to_string(subject: any) -> str:
    subject_type = type(subject)
    if subject_type == int or subject_type == float:
        return str(subject).replace('.','')
    raise TypeError('%s is not a supported type' % type(subject))
    


def _verify_str_is_palindrome(subject: str) -> bool:
    if subject[::-1] == subject:
        return True
    return False



def is_palindrome(subject: any) -> bool:
    if type(subject) != str:
        subject = _convert_to_string(subject)
    if len(subject) < 2:
        return False
    subject = subject.lower()
    return _verify_str_is_palindrome(subject)
