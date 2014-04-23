from collections import MutableSequence
from phone_book.listing import Listing, InvalidPhone


class Book(MutableSequence):
    """ Extension of mutable sequence(list) as a phone book. Creates a hash table alongside
    the phone book for quick searching of phone numbers. Hash table is limited to 100 entries and
    no collision handling is implemented.

    Phone Book concepts: Unique Numbers, Possibly Duplicate Names

    List stays sorted after all changes such as insert or append.

    __delitem, __setitem__ are not implemented
    """

    def __init__(self):
        self.data = []
        self.hash_num = [None for i in range(100)] # hash table of numbers
        self.hash_name = [None for i in range(100)] # hash table of names

    def __delitem__(self, i):
        """
        Delete method is not implemented per assignment
        """
        # # Delete from hash table
        # self.hash_num[hash(self.data[i])] = None
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
            while pos > 0 and self.data[pos - 1] > value:
                self.data[pos] = self.data[pos - 1]
                pos -= 1
            self.data[pos] = value

    def insert(self, i, item):
        """
        Insert listing into phone book and hash table.
        Checks that item is of type: Phone
        """
        # TODO: Check if phone number in book...
        # TODO: Handle Hash Table Collisions
        if isinstance(item, Listing):
            # Insert into list
            self.data.insert(i, item)
            # Insert into hash table
            self.hash_num[hash(item)] = item
            self.hash_name[hash(item['name'])%100] = item # uses default string hash
            # Sort list
            self.sort()
        else:
            raise TypeError('Did not pass object of type: Phone')

    def append(self, item):
        """ Point to insert at end
        """
        self.insert(len(self.data), item)

    def hash_table(self, type='num'):
        """ Returns the hash table
        :param type: num or name
        """
        if type == 'num':
            return self.hash_num
        elif type == 'name':
            return self.hash_name
        else:
            raise ValueError

    def lookup(self, name, method='binary'):
        """
        Custom method to lookup person in phone book by name and return listing.
        Defaults to binary lookup, but can use sequential.
        Binary and hash search finds first listing found or False if none.
        Sequential finds all matching and returns as a list if multiple.
        """
        results = []
        if method == 'hash':
            # compute hash of string using default hash function for strings
            h = hash(name) % 100
            # is entry in hash table, check if same
            if self.hash_name[h] is not None and self.hash_name[h]['name'] == name:
                return self.hash_name[hash(name) % 100]
            else:
                return False
        elif method == 'binary':
            #Binary search returns first listing found.
            low = 0
            hi = len(self.data) - 1
            while low <= hi:
                m = (low + hi) // 2
                if self.data[m]['name'] == name:
                    return self.data[m]
                elif name < self.data[m]['name']:
                    hi = m - 1
                elif name > self.data[m]['name']:
                    low = m + 1
            return False

        elif method == 'sequential':
            # Sequential search finds all matching names
            for listing in self.data:
                if listing['name'] == name:
                    results.append(listing)
            # Return Result(s) of Search
            if len(results) == 1:
                return results[0]
            elif len(results) > 1:
                return results
            else:
                return False
        else:
            raise ValueError('valid methods: sequential or binary')

    def reverse_lookup(self, num, method='hash'):
        """
        Method for reverse lookup by phone number. First checks that num is actually a valid phone number.
        Default uses hash table for quick lookup and returns the listing if it exists or False if it does not.
        May use sequential search method.
        :param method: 'hash' or 'sequential'
        :return type: Listing or False
        """
        try:
            p = Listing(num, None)
        except InvalidPhone:
            raise InvalidPhone
        if method == 'hash':
            h = hash(p)
            if self.hash_num[h] is not None:
                return self.hash_num[h]
            else:
                return False
        elif method == 'sequential':
            # sequential
            for listing in self.data:
                if listing['num'] == p['num']:
                    return listing
            return False
        else:
            raise ValueError('valid methods: sequential or hash')
