def isEven(a):
	
	if a % 2 == 0:
		return True

	return False

print(isEven(0))
print(isEven(8))
print(isEven(9))

for i in range(0 ,100 ,1):
	print(str(i)+ " is " +str(isEven(i)))

###########################

def first_last6(nums):
  
  return nums[0] == 6 or nums[len(nums) -1] == 6


############################