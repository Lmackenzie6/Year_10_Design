word = "SHINS"

def check(char):
	if (char != "I" or "O" or "S" or "H" or "Z" or "X" or "N"):
		return False
		break
	else:
		return True


for i in range(len(word)):
	print(word[i])


	if (check(word[i]) == False):
		print("NO")
		break

print("YES")



