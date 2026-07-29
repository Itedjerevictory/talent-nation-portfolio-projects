import numbers


def count_down(numbers):
    count = []
    for i in numbers:
        if i != 0:
            count.append(i)
    return count

total = count_down([5, 4, 3, 2, 1, 0])
print(total)
