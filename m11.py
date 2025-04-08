from functions import *
import unittest

class TestPrime(unittest.TestCase):
    def test_primes(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
    def test_non_primes(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))

class TestRemove(unittest.TestCase):
    def test_removes(self):
        self.assertEqual(remove_vowels("aeiou"), "")
