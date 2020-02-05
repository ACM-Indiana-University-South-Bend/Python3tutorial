#kattis_R2
#Josh Barrett, using Python3
#The number S is called the mean of two numbers R1 and R2 if S 
#is equal to (R1+R2)/2. Mirko’s birthday present for Slavko was 
#two integers R1 and R2. Slavko promptly calculated their mean 
#which also happened to be an integer but then lost R2! Restore R2.

in_str = input()
R1, S = in_str.split(' ')
R2 = 2 * int(S) - int(R1)
print (R2)
