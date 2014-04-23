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
print('Method: {0}\n Search: {1}\n Result: {2}\n'.format('sequential', '6145029096',
                                                         bk.reverse_lookup('6145029096', method='sequential')))
print('Method: {0}\n Search: {1}\n Result: {2}\n'.format('hash', 6145029096,
                                                         bk.reverse_lookup(6145029096, method='hash')))
print('*' * 5 + 'End Reverse Lookup ' + '*' * 26)

print(len(bk.hash_table(type='name')))

# # Print Hash Tables Out
# print('\n' + '*' * 50)
# print('Hash Table of Names:')
# print('*' * 50)
# for listing in bk.hash_table(type='name'):
#     if listing is not None:
#         print(hash(listing))
# print('*' * 5 + 'End Hash Table ' + '*' * 40)
#
# print('\n' + '*' * 50)
# print('Hash Table of Numbers:')
# print('*' * 50)
# for listing in bk.hash_table(type='num'):
#     if listing is not None:
#         print('hash: {0} squared: {1} number: {2}'.format(hash(listing), int(listing['num']*listing['num']), listing['num']))
# print('*' * 5 + 'End Hash Table ' + '*' * 40)
