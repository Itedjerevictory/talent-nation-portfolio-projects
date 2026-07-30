temps_celsius = [0, 20, 37, 100]
result = list(map(lambda x:  x * 9/5 + 32, temps_celsius))
print(result)






# Use map() with a lambda to convert every value to Fahrenheit. Formula: F = C * 9/5 + 32