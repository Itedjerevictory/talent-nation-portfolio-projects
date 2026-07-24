import keyword

# Check if a word is a keyword
print(keyword.iskeyword("if"))      # True
print(keyword.iskeyword("hello"))   # False
print(keyword.iskeyword("for"))     # True
print(keyword.iskeyword("my_var"))  # False