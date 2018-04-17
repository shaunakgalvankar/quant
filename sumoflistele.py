#sum of the elements in a list
string=input("enter the numbers ").split()
a=list(map(int,string))
def sum(l):
	s=0
	for i in range(len(l)):
		
		s=s+l[i]
	return s
b=sum(a)

print(b)
