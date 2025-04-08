from functions import *
import unittest

class TestPrime(unittest.TestCase):
    def test_primes(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(2))

class TestPrime2(unittest.TestCase):
    def test_non_primes(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(-4))
        self.assertFalse(is_prime(1))

class TestRemove(unittest.TestCase):
    def test_removes(self):
        self.assertEqual(remove_vowels("aeiou"), "")
        self.assertEqual(remove_vowels("AEIOU"), "")
