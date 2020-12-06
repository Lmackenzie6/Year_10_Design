import tkinter as tk
import os
from PIL import Image, ImageTk
import csv
from tkinter import messagebox


#number associated with each variable defines which row it is in

root = tk.Tk()

root.title("ATL Tracker")

Student = tk.StringVar()
ATL = tk.StringVar()
Grade = tk.StringVar()

fieldnames = ['Student', 'ATL', 'Grade']

#gradereader = csv.DictReader(file)


def SubmitGrade():
	file = open('database.csv', 'a+')
	gradewriter = csv.DictWriter(file, fieldnames = fieldnames)
	gradewriter.writerow({'Student': Student.get(), 'ATL': ATL.get(), 'Grade':Grade.get()})
	file.close()
	Student.set('')
	ATL.set('')
	Grade.set('')

def on_closing():
	print("closing")
	if messagebox.askokcancel("Quit", "Would you like to terminate the program?"):


		root.destroy()

print("Start program")
root.configure(bg="#233C6A")

#variables
path = '1200px-Upper_Canada_College_Crest.svg.jpg'

img = ImageTk.PhotoImage(Image.open(path))

panelA = tk.Label(root, image = img, highlightthickness=0)
panelB = tk.Label(root, image = img, highlightthickness=0)
L = tk.Label(root, fg="#233C6A", text="Welcome to the ATL Tracker!", bg="#2fbc2f", font=("Helvetica", "55"))
canvas1 = tk.Canvas(root, width=25, height=50, bg = "#233C6A", highlightthickness=0)
studentlabel2 = tk.Label(root, text="Student Name", bg="#2fbc2f", font="Helvetica", fg="#233C6A")
canvas4 = tk.Canvas(root, width=25, height=25, bg = "#233C6A", highlightthickness=0)
studentlabel5 = tk.Label(root, text="ATL",font="Helvetica", bg="#2fbc2f", fg="#233C6A")
canvas8 = tk.Canvas(root, width=25, height=25, bg = "#233C6A", highlightthickness=0)
label3 = tk.Label(root,text="Dropdown soon",fg="#233C6A", bg="#233C6A", font="Helvetica")
studentlabel8 = tk.Label(root, text=" MYP Grade",font="Helvetica", bg="#2fbc2f", fg="#233C6A")
canvas7 = tk.Canvas(root, width=25, height=25, bg = "#233C6A", highlightthickness=0)
canvas9 = tk.Canvas(root, width=25, height=25, bg = "#3b5482", highlightthickness=1)
canvas13 = tk.Canvas(root, width=25, height=25, bg = "#233C6A", highlightthickness=0)
canvas14 = tk.Canvas(root, width=25, height=25, bg = "#233C6A", highlightthickness=0)
canvas15 = tk.Canvas(root, width=25, height=25, bg = "#233C6A", highlightthickness=0)
variablestudents = tk.IntVar(root)
StudentVar = tk.Entry(root, textvariable=Student)
variableatl = tk.IntVar(root)
ATLVar = tk.Entry(root, textvariable=ATL)
GradeVar = tk.Entry(root, textvariable=Grade)


button16 = tk.Button(text="Submit Grade", highlightbackground="#EE5E36", fg="#233C6A", command = SubmitGrade)
#end of variables



panelA.grid(row = 0, column = 0)
panelB.grid(row = 0, column = 5)

L.grid(row = 0, column = 1, columnspan = 4)

canvas1.grid(row=1, column=2)

studentlabel2.grid(row=2, column= 2)
canvas4.grid(row=4, column=2)
studentlabel5.grid(row=5, column= 2)
canvas8.grid(row=8, column=2)


label3.grid(row=3, column=1)


studentlabel8.grid(row=8, column= 2)
canvas7.grid(row=7, column=2)
canvas9.grid(row=9, column=2)
canvas13.grid(row=13, column=2)
canvas14.grid(row=14, column=2)
canvas15.grid(row=15, column=2)

#dropdown code
variablestudents.set("Students") # default value

StudentVar.config(fg="#233C6A", highlightbackground="#233C6A", font =("Franklin Gothic", "15"))
StudentVar.grid(row=3, column=2)



variableatl.set("ATL's") # default value

ATLVar.config(fg="#233C6A", highlightbackground="#233C6A", font =("Franklin Gothic", "15"))
ATLVar.grid(row=6, column=2)

GradeVar.grid(row=9, column=2)


button16.grid(row=16, column=2)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
print ("End program")

