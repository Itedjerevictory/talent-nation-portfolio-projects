Lesson Overview
Suppose you are running your morning coffee cart. You have three data-management tasks to complete before opening:

The Wooden Flavor Rack (List): You have a list of base syrup pump counts [1, 2, 3], and you need to generate a new list where every count is doubled for double-shot recipes.
The Menu Whiteboard (Dictionary): You have a dictionary mapping drinks to prices {"Latte": 4.50, "Espresso": 3.50}, and you need to apply a ₦0.50 morning discount to every single price in-place.
The Specials Tray (Set): You have a messy set of unique display spices {" cinnamon ", "cocoa ", "cinnamon"} and you need to strip off the extra spaces and capitalize them all.
Without comprehensions, your barista robot has to write long, nested loops for each task: creating empty target variables, iterating over lists, modifying items, and appending them one by one. This is slow, repetitive, and hard to read.





Concept	Plain-Language Explanation	Storyline Reference

Comprehension	A concise Python syntax that creates a new collection by evaluating an inline loop over an existing collection.
List Comprehension	Generating a new list using the syntax: [expression for item in iterable].
Filtered Comprehension	Adding a trailing if statement to a comprehension to only process items that evaluate to True.
Dictionary Comprehension	Generating a new dictionary using the syntax: {key_expr: value_expr for key, value in dict.items()}.
Set Comprehension	Generating a new unique set using the syntax: {expression for item in iterable}.