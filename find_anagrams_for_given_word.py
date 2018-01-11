
l=raw_input('Enter: ')
alternatives = ['act', 'mat', 'rat', 'cat']
word=sorted(l)
for i in alternatives:
    if word==sorted(i):
        print i