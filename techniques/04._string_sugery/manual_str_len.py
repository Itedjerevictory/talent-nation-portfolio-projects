def str_len(value):

    #currently, the function is counting the number of characters in the string by iterating through each character and incrementing a counter. This is a manual implementation of the string length calculation.
    count = 0

    # search through each character in the string and increment the count for each character found
    for i in value:
        count = count + 1

        #return the final count after iterating through the entire string
    return count








# ManualStringLength
# Instructions
# Implement str_len(value) without using len(). Count the characters manually and return the number of characters in the string.