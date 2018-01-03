################################################################################################################
################################## CREATED BY    : PRAMODH
################################## CREATED DATE  : 25/12/2017
################################## DESCRIPTION   : THIS PROGRAM IS TO PRINT DIAMOND SHAPE
################################################################################################################

#!/usr/bin/python
side = int(input("Please input side length of diamond: "))

#for x in list(range(10)):
for x in list(range(side)) + list(reversed(range(side-1))):
    print('{: <{w1}}{:*<{w2}}'.format('', '', w1=side-x-1, w2=x*2+1))







'''i=0
j=1
while i<=j:
#  print ("*")
  i +=1
while(j>i+1):
    print("*")
    print("*")
    j +=1
#    i +=1 '''

