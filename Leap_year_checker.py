# Python program to check if year is a leap year or not

year = int(input("Enter Year to check")) # this will take input from user



if (year % 4) == 0:        #for correct output here instead of division modulus is axpected for correct output
   if (year % 100) == 0:   #instead of 10 use 100   
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
