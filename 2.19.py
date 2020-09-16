# Daniel Torres
# PSID: 1447167
# Zybooks 2.19

print('Enter amount of lemon juice (in cups):')
lemon_juice = int(input())

print('Enter amount of water (in cups):')
water = int(input())

print('Enter amount of agave nectar (in cups):')
agave_nectar = float(input())

print('How many servings does this make?\n')
servings = float(input())

print('Lemonade ingredients - yields', '{:.2f}'.format(servings),'servings')
print('{:.2f}'.format(lemon_juice),'cup(s) lemon juice')
print('{:.2f}'.format(water),'cup(s) water')
print('{:.2f}'.format(agave_nectar),'cup(s) agave nectar\n')

print('How many servings would you like to make?\n')
servings_2 = float(input())

print('Lemonade ingredients - yields', '{:.2f}'.format(servings_2),'servings')

servings_divide = (servings_2/servings)
lemonjuice_cal = servings_divide * lemon_juice
water_cal = servings_divide * water
agavenectar_cal = servings_divide * agave_nectar

print('{:.2f}'.format(lemonjuice_cal),'cup(s) lemon juice')
print('{:.2f}'.format(water_cal),'cup(s) water')
print('{:.2f}'.format(agavenectar_cal),'cup(s) agave nectar\n')


gallon = 16

lemon_gallon = lemonjuice_cal/ gallon
water_gallon = water_cal/gallon
agave_nectar_gallon = agavenectar_cal / gallon

print('Lemonade ingredients - yields', '{:.2f}'.format(servings_2),'servings')
print('{:.2f}'.format(lemon_gallon),'gallon(s) lemon juice')
print('{:.2f}'.format(water_gallon),'gallon(s) water')
print('{:.2f}'.format(agave_nectar_gallon),'gallon(s) agave nectar')