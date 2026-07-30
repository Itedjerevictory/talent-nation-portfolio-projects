def sum_stack(mugs):
    if mugs <= 0:
        return 0
    return mugs + sum_stack(mugs - 1)

print(sum_stack(4))