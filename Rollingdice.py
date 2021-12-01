from tkinter import *
import random

#main window, size, add title, background color
root = Tk()
root.title("Rolling Dice")
root.geometry("500x500")
root.configure(bg = "#E6E6FA")

label= Label (root, text="", font=("times", 260))


def roll ():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684' , '\u2685']
    label.configure(text=f"{random.choice(dice)}{random.choice(dice)}")
    label.pack()
    
#button
button = Button(root, text= "lets roll dice...", width=40, height=5, font=10, bg="white",  bd=2)
button.pack(padx=10, pady=10)

root.mainloop()