import unittest
import palindrome


class TestPalindrome(unittest.TestCase):
    def test_is_true_if_word_is_palindrome(self):
        self.assertTrue(palindrome.is_palindrome("racecar"))

    def test_is_false_if_word_is_not_palindrome(self):
        self.assertFalse(palindrome.is_palindrome("penguin"))

    def test_can_identify_numeric_palindromes(self):
        self.assertTrue(palindrome.is_palindrome(9009))
