import unittest
import palindrome


class TestPalindrome(unittest.TestCase):
    def test_is_true_if_word_is_palindrome(self):
        self.assertTrue(palindrome.is_palindrome("racecar"))

    def test_is_false_if_word_is_not_palindrome(self):
        self.assertFalse(palindrome.is_palindrome("penguin"))

    def test_can_identify_numeric_palindromes(self):
        self.assertTrue(palindrome.is_palindrome(9009))

    def test_single_character_string_is_not_a_palindrome(self):
        self.assertFalse(palindrome.is_palindrome('a'))

    def test_numerical_palindromes_ignore_decimal_point(self):
        self.assertTrue(palindrome.is_palindrome(900.9))

    def test_case_is_ignored(self):
        self.assertTrue(palindrome.is_palindrome('RaceCar'))

    def test_incorrect_input_type_throws_error(self):
        with self.assertRaises(TypeError):
            palindrome.is_palindrome(True)
