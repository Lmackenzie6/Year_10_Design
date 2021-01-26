def calculateGroup():
	first = input()
	second = input()
	third = input()
	fourth = input()
	fifth = input()
	sixth = input()


var win_counter == 0

if first == "w":
	win_counter = win_counter + 1

if second == "w":
	win_counter = win_counter + 1

if third == "w":
	win_counter = win_counter + 1

if fourth == "w":
	win_counter = win_counter + 1

if fifth == "w":
	win_counter = win_counter + 1

if sixth == "w":
	win_counter = win_counter + 1

if win_counter == 0:
	print("-1")

if win_counter == 5 or win_counter == 6:
	print("1")

if win_counter == 3 or win_counter == 4:
	print("2")

if win_counter == 1 or win_counter == 2:
	print("3")
	




calculateGroup()