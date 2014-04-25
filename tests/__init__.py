import unittest
from phone_book import Listing, Book, InvalidPhone


class TestListing(unittest.TestCase):
    def test_hash(self):
        hash_length = 100
        p1 = Listing(9287749178, 'Test', hash_length)
        self.assertEqual(hash(p1), 93)


class TestBook(unittest.TestCase):
    def setUp(self):
        self.bk = Book()

    def tearDown(self):
        pass

    def test_add(self):
        self.bk.add(9287749178, 'Flagstaff Soap Company LLC')
        self.assertEqual(len(self.bk), 1)
        self.bk.add(9287749170, 'Test')
        self.bk.add(9287749171, 'Another Test')
        self.assertEqual(len(self.bk), 3)

    def test_add_invalid(self):
        self.assertRaises(InvalidPhone, self.bk.add, 1, 'Test')
        self.assertRaises(InvalidPhone, self.bk.add, '928774917A', 'Test')
        self.assertRaises(InvalidPhone, self.bk.add, 19287749178, 'Test')

    def test_sorts_on_add(self):
        self.bk.add(9287749178, 'Flagstaff Soap Company LLC')
        self.bk.add(9287749170, 'Test')
        self.bk.add(9287749171, 'Another Test')
        self.assertEqual(self.bk[0]['num'], 9287749171)
        self.assertEqual(self.bk[1]['num'], 9287749178)
        self.assertEqual(self.bk[2]['num'], 9287749170)
        self.assertEqual(self.bk[0], sorted(self.bk)[0])

    def test_settings(self):
        self.bk.configure(HASH_TABLE_LENGTH=10)
        self.assertEqual(self.bk.settings()['HASH_TABLE_LENGTH'], 10)
        self.bk.add(9287749170, 'Test')
        self.assertEqual(len(self.bk.hash_table('num')), 10)
        # should raise error if hash table already instantiated
        self.assertRaises(Exception, self.bk.configure, HASH_TABLE_LENGTH=1000)

    def test_reverse_lookup(self):
        self.bk.add(9287749178, 'Flagstaff Soap Company LLC')
        self.assertTrue(self.bk.reverse_lookup(9287749178, method='sequential'))
        self.assertTrue(self.bk.reverse_lookup(9287749178, method='hash'))

    def test_lookup(self):
        self.bk.configure(HASH_TABLE_LENGTH=1000)  # try to avoid collisions
        self.bk.add(9287749178, 'Flagstaff Soap Company LLC')
        self.bk.add(9287749170, 'Test')
        self.bk.add(9287749171, 'Another Test')
        self.assertTrue(self.bk.lookup('Test', method='sequential'))
        self.assertTrue(self.bk.lookup('Test', method='binary'))
        self.assertTrue(self.bk.lookup('Test', method='hash'))

if __name__ == '__main__':
    unittest.main()