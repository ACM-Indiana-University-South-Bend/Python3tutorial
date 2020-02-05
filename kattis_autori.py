#kattis_autori
#Josh Barrett, using Python3
#Problem Desc: https://open.kattis.com/problems/autori

in_str = input()
names = in_str.split("-")
for n in names:
	print(n[0], end = '')
print() # to add newline
