# blind string printing
word = 'stubborn'
letter = 'b'

print(['_' if i != letter else i for i in word])

print('-'*80)

# alphabet letter printing
numbers = [5,2,5,2,2,2]
for num in numbers:
    print('$' * num)

