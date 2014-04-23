"""
Listing for a phone book.
"""

from collections import MutableMapping
import math

class InvalidPhone(Exception):
    """This exception is raised when the phone number is not of the appropriate type or format.
    Must be either a 10 digit integer or a string with only integers.
    """
    pass


class Listing(MutableMapping):
    """
    Phone number class around a mapping with an associated name.

    Listings are sorted by name property.
    """

    def __init__(self, num, name):
        """
        Two basic checks for valid phone number.
        1. Is it an int or easily converted to one?
        2. Is it a 10 digit number?
        Note: these checks are strict and not entirely practical for all regions.

        :param num: the phone number in either a string with only numbers or an integer
        :param name: name of listing
        """
        try:
            num = int(num)
        except ValueError:
            raise InvalidPhone('invalid characters')
        else:
            if num < 1000000000:
                raise InvalidPhone('too few digits')
            elif num > 9999999999:
                raise InvalidPhone('too many digits')
            else:
                self.data = {'num': num,
                             'name': name}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __hash__(self):
        """
        The hash is based on the mid square method of the phone number.
        """
        # square it
        h = self.data['num'] * self.data['num']
        # get number of digits
        digits = int(math.log10(h)) + 1
        # if odd number of digits, add leading zero
        if digits % 2 == 1:
            digits += 1
        # extract middle two digits
        h = int(h // 10 ** ((digits / 2) - 1)) % 100
        return h

    def __str__(self):
        return self.data.__str__()

    """
    Rich comparisons are made on key: 'name' since phone book listings are only sorted by name.
    """
    def __lt__(self, other):
        if 'name' in other:
            return self.data['name'] < other['name']
        else:
            raise TypeError('unorderable types')

    def __le__(self, other):
        if 'name' in other:
            return self.data['name'] <= other['name']
        else:
            raise TypeError('unorderable types')

    def __eq__(self, other):
        if 'name' in other:
            return self.data['name'] == other['name']
        else:
            raise TypeError('unorderable types')

    def __ge__(self, other):
        if 'name' in other:
            return self.data['name'] >= other['name']
        else:
            raise TypeError('unorderable types')

    def __gt__(self, other):
        if 'name' in other:
            return self.data['name'] > other['name']
        else:
            raise TypeError('unorderable types')

    def __ne__(self, other):
        if 'name' in other:
            return self.data['name'] != other['name']
        else:
            raise TypeError('unorderable types')

