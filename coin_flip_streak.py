import random
numberOfStreaks = 0
for experimentNumber in range(10):
    # Code that creates a list of 100 'heads' or 'tails' values.
    list_flips = []
    for i in range(100):
        random_int = random.randint(0,1)
        if random_int == 1:
            list_flips.append('H')
        else:
            list_flips.append('T')
    # Code that checks if there is a streak of 6 heads or tails in a row.
    seq = ''.join(list_flips)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))