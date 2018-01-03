##########################################################################################################
########################### CREATED BY     : PRAMODH
########################### CREATED DATE   : 25/12/2017
########################### DESCRIPTION    : TO PRINT WHETHER THE GIVEN NUMBER IS FIBONACCI 
##########################################################################################################

#!/usr/bin/python
#prevnum =0
#curnum=1
#count =0
#while count < 10:
#       print(prevnum,end=' , ')
#       nth = prevnum + curnum
#       # update values
#       prevnum = curnum
#       curnum = nth
#       count += 1


# change this value for a different result
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1)     
   #   print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
