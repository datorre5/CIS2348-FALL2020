#Daniel Torres
#PSID:1447167


def selection_sort_descend_trace(numbers):
    length = len(numbers)

    for i in range(length):

        max_index = i
        for j in range(i + 1, length):
            if numbers[max_index] < numbers[j]:
                max_index = j

        if max_index == i:
            break


        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]


        for x in numbers:
            print(x, end=' ')
        print()

if __name__ == "__main__":
    numbers = []
    num = input().split(' ')
    numbers.extend(num)

    selection_sort_descend_trace(numbers)