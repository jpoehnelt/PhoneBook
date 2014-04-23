from collections import MutableSequence
from phone_book.listing import Listing, InvalidPhone


class Book(MutableSequence):
    """ Extension of mutable sequence(list) as a phone book. Creates a hash table alongside
    the phone book for quick searching of phone numbers. Hash table is limited to 100 entries and
    no collision handling is implemented.

    __delitem, __setitem__ are not implemented
    """

    def __init__(self):
        self.data = []
        self.hash = [None for i in range(100)]

    def __delitem__(self, i):
        """
        Delete method is not implemented per assignment
        """
        # # Delete from hash table
        # self.hash[hash(self.data[i])] = None
        # # Delete from list
        # self.data.__delitem__(i)
        pass

    def __setitem__(self, i, item):
        """
        Set method is not implemented per assignment
        """
        pass

    def __getitem__(self, item):
        return self.data.__getitem__(item)

    def __len__(self):
        return self.data.__len__()

    def __sort__(self):
        """
        Implementation of insertion sort.
        """
        for i in range(1, len(self.data)):
            value = self.data[i]
            pos = i
            print(self.data[pos - 1]['name'])
            while pos > 0 and self.data[pos - 1] > value:
                self.data[pos] = self.data[pos - 1]
                pos -= 1
            self.data[pos] = value
        return self

    def sort(self):
        """
        Implementation of insertion sort.
        """
        for i in range(1, len(self.data)):
            value = self.data[i]
            pos = i
            print(self.data[pos - 1]['name'])
            while pos > 0 and self.data[pos - 1] > value:
                self.data[pos] = self.data[pos - 1]
                pos -= 1
            self.data[pos] = value

    def insert(self, i, item):
        """
        Insert phone into phone book and hash table.
        Checks that item is of type: Phone
        """
        if isinstance(item, Listing):
            # Insert into list
            self.data.insert(i, item)
            # Insert into hash table
            self.hash[hash(item)] = item
        else:
            raise TypeError('Did not pass object of type: Phone')

    def append(self, item):
        """ Point to insert at end
        """
        self.insert(len(self.data), item)

    def hash_table(self):
        """ Returns the hash table
        """
        return self.hash

    def lookup(self, name, method='binary'):
        """
        Custom method to lookup person in phone book by name and return listing.
        Defaults to binary lookup, but can use sequential. Returns listing if found or False if not.
        """
        if method == 'binary':
            pass
        elif method == 'sequential':
            for listing in self.data:
                print(listing)
                if listing['name'] == name:
                    return listing
            return False
        else:
            raise ValueError('valid methods: sequential or binary')

    def reverse_lookup(self, num):
        """
        Method for reverse lookup by phone number. First checks that num is actually a valid phone number.
        Uses hash table for quick lookup and returns the listing if it exists or False if it does not.
        """
        try:
            p = Listing(num)
        except InvalidPhone:
            raise InvalidPhone

        h = hash(p)
        if self.hash[h] is not None:
            return self.hash[h]
        else:
            return False