# Daniel Torres
# PSID: 1447167
# Zybooks 5.19

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

service1_cost = 0
service2_cost = 0

service_1 = input('Select first service:\n')
service_2 = input('Select second service:')

print("")

if service_1 == 'Oil change':
    service1_cost = 35
elif service_1 == 'Tire rotation':
    service1_cost = 19
elif service_1 == 'Car wax':
    service1_cost = 12
elif service_1 == 'Car wash':
   service1_cost = 7



if service_2 == 'Oil change':
    service2_cost = 35
elif service_2 == 'Tire rotation':
    service2_cost = 19
elif service_2 == 'Car wax':
    service2_cost = 12
elif service_2 == 'Car wash':
    service2_cost = 7


print("")

print("Davy's auto shop invoice\n")
if service_1 == '-':
    print('Service 1: No service')
else:
    print('Service 1: '+ service_1 +', '+ '$' + str(service1_cost))
if service_2 == '-':
    print('Service 2: No service')
else:
    print('Service 2: '+ service_2 + ', '+'$' + str(service2_cost))

print("")
print('Total: $'+str(service1_cost + service2_cost))
