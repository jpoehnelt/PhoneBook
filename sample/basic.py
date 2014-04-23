from phone_book import Book, Listing



p1 = Listing(6145029096, 'Justin')
p2 = Listing(9288531234, 'Tim')
p3 = Listing(9288531216, 'John')
p4 = Listing(9281531212, 'Mary')
p5 = Listing(1234567890, 'Zach')
bk = Book()
bk.append(p1)
bk.append(p2)
bk.append(p3)
bk.append(p4)
bk.append(p5)

for listing in bk:
    print(listing)
bk.sort()
for listing in bk:
    print(listing)
#print(bk.lookup('Justin'))
#print(bk.reverse_lookup(6145029096))
#
print('hash table')
for listing in bk.hash_table():
    print(listing)

