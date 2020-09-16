# Daniel Torres
# PSID : 1447167
# HW 1
print('Birthday Calculator')

print('Current date')

print('Month:')
current_month = int(input())
print('Day:')
current_day = int(input())
print('Year:')
current_year = int(input())

current_date = (current_month,'/',current_day)

print('Birthday')

print('Month:')
birth_month = int(input())
print('Day:')
birth_day = int(input())
print('Year:')
birth_year = int(input())

birth_date = (birth_month, '/',birth_day)

age = current_year - birth_year

if(current_date == birth_date):
    print('HAPPY BIRTHDAY!!!!')

else:
    print('You are',age, 'years old.')



