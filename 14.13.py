#Daniel Torres
#PSID: 1447167


num_calls = 0


def partition(user_ids, i, k):
    index = (i - 1)
    pivot = user_ids[k]

    for j in range(i, k):

        if user_ids[j] < pivot:
            index += 1
            user_ids[index], user_ids[j] = user_ids[j], user_ids[index]

    user_ids[index + 1], user_ids[k] = user_ids[k], user_ids[index + 1]
    return i + 1


def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1

    if i < k:
        pi = partition(user_ids, i, k)

        quicksort(user_ids, i, pi - 1)
        quicksort(user_ids, pi + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls)

    for user_id in user_ids:
        print(user_id)
