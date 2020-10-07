#Daniel Torres
#PSID:1447167
#HW 2: part b


#part b
def main(date):

   month_of_number = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,
              "August":8,"September":9,"October":10,"Novenber":11,"December":12}
   try:
      year = date.split(",")[-1].strip()
      month = date.split(",")[0].split()[0]
      day = date.split(",")[0].split()[-1]
      month_number = month_of_number[month]
      int(year)
      int(day)

      return str(month_number)+"/"+day+"/"+year
   except:
      return ""

with open("inputDates.txt") as f:
   for x in f.readlines():
      if x.strip() != "-1":
         print(main(x.strip()))
