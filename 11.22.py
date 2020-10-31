words = input()
words = words.split(" ")
freq = {}

for each in words:
    if each in freq:
        freq[each] = freq[each] + 1
    else:
        freq[each] = 1
for each in words:
    print(each, freq[each])
