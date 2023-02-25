from tkinter import *
import random
import string
from tkinter import messagebox

window = Tk()

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation


def generate_password():
    resultL.delete(0, "end")
    
    try:
        ln = int(lenBtn.get())
    except ValueError:
        error = messagebox.showerror("Try again!", "Incorrect value, Integer only!")
        
    all = lower + upper + numbers + symbols
    password = [random.choice(all) for l in range(ln)]
    resultL.insert(0, "".join(password))
    

def reset_values():
    resultL.delete(0, "end")

resultL = Entry(window, 
                text="Result", 
                width=51, 
                bg="lightgrey",
                font=20)
resultL.place(x=20, y=70)

lenBtn = Entry(window, 
               text="Length", 
               width=10, 
               bg="lightgrey",
               font=20)
lenBtn.place(x=20, y=120)

lenStr = Label(window, 
               text="Length")
lenStr.place(x=20, y=140)


numBtn = Button(window, 
                   text="Submit", 
                   width=10, 
                   height=2, 
                   bg="lightgrey", 
                   command=generate_password)
numBtn.place(x=200, y=118)

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
                  bg="lightgrey",
                  command=reset_values)
resetBtn.place(x=400, y=118)

window.title("Arsalan's Password Generator")
window.geometry("502x200")
window.resizable(0, 0)
window.attributes("-topmost", True)
window.mainloop()
