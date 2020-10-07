#Daniel Torres
#PSID: 1447167
#Zybooks 7.25





def exact_change(total):
    dollars = total // 100
    total %= 100
    quarters = total // 25
    total %= 25
    dimes = total // 10
    total %= 10
    nickels = total // 5
    total %= 5
    pennies = total
    return dollars, quarters, dimes, nickels, pennies
def main():
    input_val = int(input())
    dollars, quarters, dimes, nickels, pennies = exact_change(input_val)
    if input_val <= 0:
        print('no change')
    else:
        if dollars > 1:
            print('%d dollars' % dollars)
        elif dollars == 1:
            print('%d dollar' % dollars)

        if quarters > 1:
            print('%d quarters' % quarters)
        elif quarters == 1:
            print('%d quarter' % quarters)

        if dimes > 1:
            print('%d dimes' % dimes)
        elif dimes == 1:
            print('%d dime' % dimes)

        if nickels > 1:
            print('%d nickels' % nickels)
        elif nickels == 1:
            print('%d nickel' % nickels)

        if pennies > 1:
            print('%d pennies' % pennies)
        elif pennies == 1:
            print('%d penny' % pennies)
if __name__ == '__main__':
    main()