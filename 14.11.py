#Daniel Torres
#PSID: 1447167


parts = input().split()
name = parts[0]
while name != '-1':


    try:
        age = int(parts[1]) + 1
    except ValueError as vs:

        age = 0


    print('{} {}'.format(name, age))


    parts = input().split()
    name = parts[0]