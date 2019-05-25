#input_string = input()
#new_string = ''
#for ch in input_string:
#    comp = ch.lower()
#    if ch.lower() not in 'aeiouy':
#        new_string += '.'+ch.lower()
#print(new_string)

print(''.join('.'+ x.lower() for x in input() if x not in 'aeiouy'))
