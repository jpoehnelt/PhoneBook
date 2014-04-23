from phone_book import Book, Listing

# create the phone book
bk = Book()

# create some listings
p1 = Listing(6145029096, 'Justin')
p2 = Listing(9288531234, 'Tim')
p3 = Listing(9288531216, 'John')
p4 = Listing(9281531212, 'Mary')
p5 = Listing(1234567890, 'Zach')
p6 = Listing(1231567890, 'Bob')
p7 = Listing('9280001111', 'Megan') # can enter as a string
p8 = Listing('9281110000', 'Sarah')

# add listings to phone book
bk.append(p1)
bk.append(p2)
bk.append(p3)
bk.append(p4)
bk.append(p5)
bk.append(p6)
bk.append(p7)
bk.append(p8)

# Lookup name and get listing
print('\n'+'*'*50)
print('Lookup (Search by Name)')
print('*'*50)
print('Method: {0}\n Search: {1}\n Result: {2}\n'.format('sequential', 'Justin', bk.lookup('Justin', method='sequential')))
print('Method: {0}\n Search: {1}\n Result: {2}\n'.format('hash', 'Justin', bk.lookup('Justin', method='hash')))
print('Method: {0}\n Search: {1}\n Result: {2}\n'.format('binary', 'Justin', bk.lookup('Justin', method='binary')))
print('*'*5 + 'End Lookup ' + '*'*34)

# Reverse lookup and get name
print('\n'+'*'*50)
print('Reverse Lookup (Search by Number)')
print('*'*50)
print('Method: {0}\n Search: {1}\n Result: {2}\n'.format('sequential', '6145029096', bk.reverse_lookup('6145029096', method='sequential')))
print('Method: {0}\n Search: {1}\n Result: {2}\n'.format('hash', 6145029096, bk.reverse_lookup(6145029096, method='hash')))
print('*'*5 + 'End Reverse Lookup ' + '*'*26)


# # Print Hash Tables Out
# print('\n'+'*'*50)
# print('Hash Table of Names:')
# print('*'*50)
# for listing in bk.hash_table(type='name'):
#      print(listing)
# print('*'*5 + 'End Hash Table ' + '*'*40)
#
# print('\n'+'*'*50)
# print('Hash Table of Numbers:')
# print('*'*50)
# for listing in bk.hash_table(type='num'):
#      print(listing)
# print('*'*5 + 'End Hash Table ' + '*'*40)
