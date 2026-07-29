def clean_username(value):
    cleaned_value = value.strip().lower().replace(" ", "_")
    return cleaned_value








# Instructions
# Implement clean_username(value). The function should remove leading and trailing spaces, convert the text to lowercase, and replace every space with an underscore. Return the cleaned username.