import unittest
from phone_book import Listing


class TestListing(unittest.TestCase):
    def test_hash(self):
        hash_length = 100
        p1 = Listing(9287749178, 'Test', hash_length)
        self.assertEqual(hash(p1),93)

if __name__ == '__main__':
    unittest.main()