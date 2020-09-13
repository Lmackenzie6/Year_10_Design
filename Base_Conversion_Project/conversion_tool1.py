import tkinter as tk

print("Stage 5")
'''





'''

def process(*args):

	val = ent_value.get()
	print(val)

	#check to ensure 1s and 0s
	check = check01(val)
	print(check)


	if (check):
		val = remove0(val)
		print(val)
		result = base2to10(val)
		lab_results.config(text = str(val) + " --> " + str(result))
	else:
		lab_results.config(text = "INVALID")


	ent_value.delete(0,tk.END)

def base2to10(str):

	n = 0
	total = 0

	for i in range(len(str) - 1, -1, -1):
			print("***",n)
			total = total + int(str[i]) * (2**n)
			print("---",total)
			n = n + 1

	return total
		

def remove0(str):
	
	for i in range (0, len(str), 1):
		if (str[i] == "1"):
			return str[i:]

	return str

def check01(str):
	num_0 = str.count("0")
	num_1 = str.count("1")

	if num_0 + num_1 == len(str):
		return True
	return False

root = tk.Tk()

lab_instructions = tk.Label(root, text = "Enter Binary")
ent_value = tk.Entry(root)
lab_results = tk.Label(root, text = "--")

lab_instructions.pack()
ent_value.pack()
lab_results.pack()

root.bind("<Return>",process)
root.mainloop()