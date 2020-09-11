import tkinter as tk

print("Stage 3")


def process(*args):
	print("process")

	val = ent_value.get()
	print(val)

	#check to ensure 1s and 0s
	check = check01(val)
	print(check)


	if (check == True):

		#Remove leftmost 0
		#Convert
		lab_results.config(text = "VALID INPUT")
	else:
		#update display with error message
		lab_results.config(text = "INVALID")


	ent_value.delete(0,tk.END)


def check01(str):
	print("Check 01")
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