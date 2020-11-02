#Daniel Torres
#PSID: 1447167



player_list = {}
list_keys = []

def DictKeys():
    list_keys = sorted(player_list.keys())
    return list_keys

def Roster():
    list_keys = DictKeys()
    print("ROSTER")

    for i in list_keys:
        print("Jersey number: " + str(i) + ", Rating: " + str(player_list[i]))

def addPlayer():
    print("Enter a new player's jersey number:")
    jersey_number = int(input())

    while ((jersey_number < 0) or (jersey_number > 99)):
        print("Invalid Jersey Number! Please " + "enter again!")
        print("Enter a new player's jersey number:")

        jersey_number = int(input())

    print("Enter the player's rating:")

    player_rating = int(input())

    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")
        print("Enter the player's rating:")

        player_rating = int(input())

    player_list.update({jersey_number: player_rating})

def removePlayer():
    print("Enter a jersey number:")
    jersey_number = int(input())


    while ((jersey_number < 0) or (jersey_number > 99)):
        print("Invalid Jersey Number! Please " + "enter again!")
        print("Enter a jersey number:")
        jersey_number = int(input())

    if jersey_number in player_list.keys():
        del player_list[jersey_number]

def updatePlayer():
    print("Enter a jersey number:")
    jersey_number = int(input())

    while ((jersey_number < 0) or (jersey_number > 99)):
        print("Invalid Jersey Number! Please " + "enter again!")
        print("Enter a jersey number:")
        jersey_number = int(input())

    print("Enter a new rating for player:")
    player_rating = int(input())

    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")

        print("Enter a new rating for player:")

        player_rating = int(input())

    player_list[jersey_number] = player_rating

def PlayerAboveRating():
    print("Enter a rating:")
    rating = int(input())

    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")
        print("Enter a rating:")
        rating = int(input())

    print("ABOVE 8")
    list_keys = DictKeys()

    for i in list_keys:
        if (player_list[i] > rating):

            print("Jersey number: " + str(i) + ", Rating: " + str(player_list[i]))

for i in range(1, 6):
    print("Enter player " + str(i) + "'s jersey number:")
    jersey_number = int(input())

    while ((jersey_number < 0) or (jersey_number > 99)):
        print("Invalid Jersey Number! Please " + "enter again!")
        print("Enter player " + str(i) + "'s jersey number:")
        jersey_number = int(input())
    print("Enter player " + str(i) + "'s rating:")

    player_rating = int(input())

    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")
        print("Enter player " + str(i) + "'s rating:")

        player_rating = int(input())

    print()

    player_list[jersey_number] = player_rating

Roster()

print()

while (True):
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()
    print("Choose an option:")
    user_choice = input()


    if (user_choice == 'a'):
        addPlayer()

    elif (user_choice == 'd'):
        removePlayer()

    elif (user_choice == 'u'):
        updatePlayer()

    elif (user_choice == 'r'):
        PlayerAboveRating()

    elif (user_choice == 'o'):
        Roster()

    elif (user_choice == 'q'):
        break

    print()


