n=int(input())
sum=0
for i in range(1,n+1,2):
	print(sum, '+', i,'=',sum+i)
	sum+=i
	print(sum)