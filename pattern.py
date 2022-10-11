
def numpat(n):
	num = 0.1

	for i in range(0, n):

		num = 0.1
	
		for j in range(0, i+1):
		
			print(num, end=" ")
			num = num + 0.1
	
		print("\r")

n = int(input("enter number of rows "))
numpat(n)
