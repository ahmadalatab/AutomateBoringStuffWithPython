import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count= {}
for letter in message:
    count.setdefault(letter, 0)
    count[letter] = count[letter] + 1
pprint.pprint(count)