#Daniel Torres
#PSID: 1447167



# Take age input form user
def get_age():
    age = int(input())  # take age input
    if 18 <= age <= 78:
        return age
    else:
        # raise a exception
        raise ValueError("Invalid age.")


# Calculate fat burning heart rate
def fat_burning_heart_rate():
    age = get_age()

    # calculate & print
    maximum_heart_rate = 220-age
    heart_rate = maximum_heart_rate * 0.7
    print('Fat burning heart rate for a', age, 'year-old:',heart_rate,'bpm')


# Main
if __name__ == '__main__':
    try:
        fat_burning_heart_rate()
    except ValueError as vs:
        print(vs)
        print('Could not calculate heart rate info.\n')

