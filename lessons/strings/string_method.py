# The common cleanup methods:
import pprint


order = "  latte  "

cleaned = order.strip()        # Removes whitespace from both ends -> "latte"
loud = order.upper()           # Converts to uppercase -> "  LATTE  "
quiet = order.lower()          # Converts to lowercase -> "  latte  "
proper = order.strip().title() # Chains methods to strip and capitalize -> "Latte"

# Replace words inside a string
message = "Your coffee is ready"
new_message = message.replace("coffee", "latte") # -> "Your latte is ready"

print("Cleaned: [" + cleaned + "]")
print("Loud: [" + loud + "]")
print("Quiet: [" + quiet + "]")
print("Proper: [" + proper + "]")
print("New Message: [" + new_message + "]")
