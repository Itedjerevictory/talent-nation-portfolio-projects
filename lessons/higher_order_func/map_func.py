names = ['ada', 'chidi', 'tunde']
prices = [100, 250, 400]
words = ['python', 'lambda', 'map']

capitalized = list(map(lambda name: name.upper(), names))
print('Uppercase:', capitalized)

discounted = list(map(lambda p: p - 20, prices))
print('Minus 20:', discounted)

lengths = list(map(lambda w: len(w), words))
print('Lengths:', lengths)

labels = list(map(lambda p: f'₦{p}.00', prices))
print('Formatted:', labels)

is_even = list(map(lambda p: p % 2 == 0, prices))
print('Is even:', is_even)









# Imagine you have a menu tray holding three drinks. You want to apply a ₦0.50 price increase to every single item.

# You try to use Python's map() tool to automate this. You write: