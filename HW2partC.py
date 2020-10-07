#Daniel Torres
#PSID: 1447167
# HW 2: part c
def main(date):

   number_of_month = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,
              "August":8,"September":9,"October":10,"Novenber":11,"December":12}
   try:
      year = date.split(",")[-1].strip()
      month = date.split(",")[0].split()[0]
      day = date.split(",")[0].split()[-1]
      month_number = number_of_month[month]
      int(year)
      int(day)
      return str(month_number)+"/"+day+"/"+year
   except:
      return ""

with open("inputDates.txt") as f:
   for x in f.readlines():
      if x.strip() != "-1":
         res = main(x.strip())
         if res != "":
            with open("parsedDates.txt","a+") as w:
               w.write(res+"\n")