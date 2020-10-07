#Daniel Torres
#PSID :1447167
# HW 2: part a



def main(date):

   month_of_number = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,
              "August":8,"September":9,"October":10,"Novenber":11,"December":12}
   year = date.split(",")[-1].strip()
   month = date.split(",")[0].split()[0]
   day = date.split(",")[0].split()[-1]
   number_of_month = month_of_number[month]
   return str(number_of_month)+"/"+day+"/"+year

while True:
   date_input= input()
   if date_input == "-1":
      break
   print(main(date_input))
