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
        self.hash_num = None # hash table of numbers
        self.hash_name = None # hash table of names
        self._settings = {
            'HASH_TABLE_LENGTH': 100
        }
    def __delitem__(self, i):
        """
        Delete method is not implemented per assignment
        """
        # # Delete from hash table
        # self.hash_num[hash(self.data[i])] = None
        # # Delete from list
        # self.data.__delitem__(i)
        raise NotImplemented

    def __setitem__(self, i, item):
        """
        Set method is not implemented per assignment
        """
        raise NotImplemented


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
        Not implemented, instead calling insertion sort after adding listing.
        """
        raise NotImplemented("try .add(number, 'name') instead")

    def append(self, item):
        """
        Not implemented, instead calling insertion sort after adding listing.
        """
        raise NotImplemented("try .add(number, 'name') instead")

    def add(self, num, name):
        """
        Add listing to phone book and hash tables.
        Phone book is resorted after new listing is added.
        """
        try:
            l = Listing(num, name, self._settings['HASH_TABLE_LENGTH'])
        except Exception as e:
            raise e

        self.data.append(l)
        try:
            self.hash_name[0]
        except TypeError as e:
            self.hash_num = [None for _ in range(self._settings['HASH_TABLE_LENGTH'])]
            self.hash_name = [None for _ in range(self._settings['HASH_TABLE_LENGTH'])]
        finally:
            self.hash_num[hash(l)] = l
            self.hash_name[hash(name) % self._settings['HASH_TABLE_LENGTH']] = l # uses default string hash
        self.sort()

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
            h = hash(name) % self._settings['HASH_TABLE_LENGTH']
            # is entry in hash table, check if same
            if self.hash_name[h] is not None and self.hash_name[h]['name'] == name:
                return self.hash_name[h]
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
            p = Listing(num, None, self._settings['HASH_TABLE_LENGTH'])
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

    def configure(self, **kwargs):
        for k, v in kwargs.items():
            if k in self._settings: # key is in settings
                if k == 'HASH_TABLE_LENGTH' and self.hash_num is not None:
                    raise Exception('Hash table already created.')
                self._settings[k]= v
            else:
                raise Exception

    def settings(self):
        return self._settings