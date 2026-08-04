raw_spices = {"  cinnamon ", "cocoa ", "cinnamon", "nutmeg"}

# set comprehension to clean up the raw_spices set by stripping whitespace and converting to lowercase
clean_spices = {spice.strip().lower() for spice in raw_spices}
print(clean_spices)


