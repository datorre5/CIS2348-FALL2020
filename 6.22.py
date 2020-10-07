#Daniel Torres
#PSID: 1447167
#Zybooks 6.22




def main():
    x1 = int(input())
    y1 = int(input())
    number_1 = int(input())

    x2 = int(input())
    y2 = int(input())
    number_2 = int(input())

    solution = False

    for x in range(-10, 11):
        for y in range(-10, 11):
            if (x1 * x + y1 * y == number_1) and (x2 * x + y2 * y == number_2):
                print(x, y)
                solution = True

    if not solution:
        print("No solution")


if __name__ == '__main__':
    main()