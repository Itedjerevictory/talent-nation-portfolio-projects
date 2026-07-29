names = ['ada', 'chidi', 'tunde', 'bo', 'eze']
prices = [100, 250, 400, 90, 45]
words = ['apple', 'banana', 'avocado', 'grape']

a_names = list(filter(lambda n: n.startswith('a'), names))
print('Starts with a:', a_names)

even_prices = list(filter(lambda p: p % 2 == 0, prices))
print('Even prices:', even_prices)

long_words = list(filter(lambda w: len(w) > 5, words))
print('Long words:', long_words)

not_ada = list(filter(lambda n: n != 'ada', names))
print('Not ada:', not_ada)

allowed = ['chidi', 'eze']
found = list(filter(lambda n: n in allowed, names))
print('In allowed list:', found)

short_a = list(filter(lambda n: len(n) <= 3 and n[0] in 'aeiou', names))
print('Short + vowel start:', short_a)


# Step 5: filter() — keeping only some items from a list

# While map() transforms every item, filter() keeps only the items that pass a test, and throws the rest away.



# filter( lambda price: price > 200 ,   prices )
#           ↑                             ↑
#    "the test — must return          "the list to
#     True or False"                   test each item from"