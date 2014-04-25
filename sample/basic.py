from phone_book import Book

# create the phone book
bk = Book()
bk.configure(HASH_TABLE_LENGTH=100)

# create some listings
bk.add(9287749178, 'Justin')
bk.add(9288531234, 'Tim')
bk.add(9288531216, 'John')
bk.add(9281531212, 'Mary')
bk.add(1234567890, 'Zach')
bk.add(1231567890, 'Bob')
bk.add('9280001111', 'Megan')  # can enter as a string
bk.add('9281110000', 'Sarah')



# Lookup name and get listing
print('\n' + '*' * 50)
print('Lookup (Search by Name)')
print('*' * 50)
print('Method: {0}\n Search: {1}\n Result: {2}\n'.format('sequential', 'Justin',
                                                         bk.lookup('Justin', method='sequential')))
print('Method: {0}\n Search: {1}\n Result: {2}\n'.format('hash', 'Justin', bk.lookup('Justin', method='hash')))
print('Method: {0}\n Search: {1}\n Result: {2}\n'.format('binary', 'Justin', bk.lookup('Justin', method='binary')))
print('*' * 5 + 'End Lookup ' + '*' * 34)

# Reverse lookup and get name
print('\n' + '*' * 50)
print('Reverse Lookup (Search by Number)')
print('*' * 50)
print('Method: {0}\n Search: {1}\n Result: {2}\n'.format('sequential', '9287749178',
                                                         bk.reverse_lookup('9287749178', method='sequential')))
print('Method: {0}\n Search: {1}\n Result: {2}\n'.format('hash', 9287749178,
                                                         bk.reverse_lookup(9287749178, method='hash')))
print('*' * 5 + 'End Reverse Lookup ' + '*' * 26)
