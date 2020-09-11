function isEven(a) {
	
	if (a % 2 == 0){
		return true;
	}

	return false;
}

print(isEven(0))
print(isEven(8))
print(isEven(9))

for i in range(0 ,100 ,1):
	print(str(i)+ " is " +str(isEven(i)))