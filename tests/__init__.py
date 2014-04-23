from unittest import TestCase
from phone_book import Listing


class TestListing(TestCase):
    def test_hash(self):
        hash_length = 100
        p1 = Listing(9287749178, 'Test', hash_length)
        self.assertEqual(hash(p1),93)