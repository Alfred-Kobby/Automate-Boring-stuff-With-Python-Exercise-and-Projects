spam = ['apples', 'bananas', 'tofu', 'cats']

for text in range(len(spam[:-1])):
    print(spam[text],  end=', ')
print('and ' + spam[-1])