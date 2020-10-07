#Daniel Torres
#PSID: 1447167
# Zybooks 8.10


name=input('')
name.replace(" ", "")
length=len(name)

def main(list):
    letter=0
    mid=length/2
    i=0
    while(i<mid):
        if(list[i]!=list[length-i-1]):
            letter=1
            break
        else:
            i=i+1
    if(letter==1):
        print(list,"is not a palindrome")
    else:
        print(list,"is a palindrome")
main(name)