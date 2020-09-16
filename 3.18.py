# Daniel Torres
# PSID: 1447167
# Zybooks 3.18

wall_height = int(input('Enter wall height (feet):\n'))

wall_width = int(input('Enter wall width (feet):\n'))

wall_area = wall_height * wall_width
print('Wall area:',wall_area,'square feet')

gallons = wall_area / 350
cans = round(gallons)
print('Paint needed:','{:.2f}'.format(gallons),'gallons')
print('Cans needed:',cans,'can(s)\n')

print('Choose a color to paint the wall:')
color = str(input())
if color == 'red':
    red_paint = cans * 35
    print('Cost of purchasing red paint:','${}'.format(red_paint))
elif color == 'blue':
        blue_paint = cans * 25
        print('Cost of purchasing blue paint:','${}'.format(blue_paint))
elif color == 'green':
    green_paint = cans * 23
    print('Cost of purchasing green paint:','${}'.format( green_paint))



