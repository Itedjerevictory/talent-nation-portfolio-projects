# To process bulk kitchen orders, you need to break single lines of text into individual items, or combine lists of ingredients back into a single display label.

# .split(separator): Breaks a string apart at every instance of the separator and returns them as a List.
# separator.join(list): Merges a list of strings back into a single string, pasting the separator between each item.
# Let us track the state of our order menu as we split and join its values.

sentence = "latte and espresso"
words = sentence.split(" and ")
print(words)
rejoined = "-".join(words)
print(rejoined)
