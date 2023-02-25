from tkinter import *
import random
import string
from tkinter import messagebox

window = Tk()

def generate_password():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    resultL.delete(0, "end")

    try:
        ln = int(lenBtn.get())
    except ValueError:
        error = messagebox.showerror("Try again!", "Incorrect value, Integer only!")
        
    all = lower + upper + numbers + symbols
    password = [random.choice(all) for l in range(ln)]
    resultL.insert(0, "".join(password))


resultL = Entry(window, 
                text="Result", 
                width=76, 
                bg="lightgrey")
resultL.place(x=20, y=70)

lenBtn = Entry(window, 
               text="Length", 
               width=10, 
               bg="lightgrey")
lenBtn.place(x=20, y=120)

lenStr = Label(window, 
               text="Length")
lenStr.place(x=20, y=140)

numBtn = Button(window, 
                text="Number", 
                width=10, 
                height=2, 
                bg="lightgrey")
numBtn.place(x=100, y=118)

spcBtn = Button(window, 
                text="Special",
                width=10, 
                height=2, 
                bg="lightgrey")
spcBtn.place(x=200, y=118)

submitBtn = Button(window, 
                   text="Submit", 
                   width=10, 
                   height=2, 
                   bg="lightgrey", 
                   command=generate_password)
submitBtn.place(x=300, y=118)

resetBtn = Button(window, 
                  text="Reset", 
                  width=10, 
                  height=2, 
                  bg="lightgrey")
resetBtn.place(x=400, y=118)

window.title("Arsalan's Password Generator")
window.geometry("502x200")
window.resizable(0, 0)
window.attributes("-topmost", True)
window.mainloop()
