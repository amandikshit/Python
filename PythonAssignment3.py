#PythonAssignment3
def checkEquality(a,b,c):
	if(a==b or a==c or b==c):
		return True
	else:
		return False
a=int(input("Enter First Number :"))
b=int(input("Enter Second Number :"))
c=int(input("Enter Third Number :"))
result=checkEquality(a,b,c)
print("Result :", result)