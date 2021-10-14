from tkinter import *
from tkinter.font import BOLD,Font
from PIL import ImageTk,Image

root = Tk()
root.title("Meal Suggester")
root.iconbitmap('C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/icons8food50.ico')
root.configure(background="#524c4c")
root.geometry("450x450+500+500")
root.resizable(width=False, height=False)



#Defining dictionary

dictOne = {"ChickenGreenBeansRice": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/cgr.png")),
"ChickenGreenBeansPasta": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/cgp.png")),
"ChickenGreenBeansPotatoes": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/cgpo.png")),
"ChickenSpinachRice": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/csr.png")),
"ChickenSpinachPasta": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/csp.png")),
"ChickenSpinachPotatoes": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/cspo.png")),
"ChickenCornRice": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/ccr.png")),
"ChickenCornPasta": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/ccp.png")),
"ChickenCornPotatoes": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/ccpo.png")),
"BeefGreenBeansRice": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/bgr.png")),
"BeefGreenBeansPasta": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/bgp.png")),
"BeefGreenBeansPotatoes": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/bgpo.png")),
"BeefSpinachRice": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/bsr.png")),
"BeefSpinachPasta": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/bsp.png")),
"BeefSpinachPotatoes": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/bspo.png")),
"BeefCornRice": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/bcr.png")),
"BeefCornPasta": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/bcp.png")),
"BeefCornPotatoes": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/bcpo.png")),
"PorkGreenBeansRice": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/pgr.png")),
"PorkGreenBeansPasta": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/pgp.png")),
"PorkGreenBeansPotatoes": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/pgpo.png")),
"PorkSpinachRice": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/psr.png")),
"PorkSpinachPasta": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/psp.png")),
"PorkSpinachPotatoes": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/pspo.png")),
"PorkCornRice": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/pcr.png")),
"PorkCornPasta" : ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/pcp.png")),
"PorkCornPotatoes": ImageTk.PhotoImage(Image.open("C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/images/pcpo.png"))}



#Defining functions for popup windows

def GetMeal():
    va=(meat.get() + veg1.get() + veg2.get())
    top = Toplevel()
    top.title("Suggested Meal")
    top.iconbitmap('C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/icons8food50.ico')
    myImage = dictOne[va]
    dictlabel = Label(top, image=myImage).pack()

def About():
    top2 = Toplevel()
    top2.title("About")
    top2.iconbitmap('C:/Users/thech/Desktop/SDEV140 Intro to Software Dev/Final Project/icons8food50.ico')
    about_label=Label(top2, text = "Meal Suggester \n Created by John Hessong - October/2021",padx=100, pady=200, background="#524c4c").pack()



#Creating labels

info_label = Label(root, text="Choose 1 Meat and 2 vegetables from the drop down menus!",background="#524c4c", font= BOLD)

#Creating buttons
about = Button(root, text="About", padx=3., bg="#000000", fg="#ffffff", command = About)
f_meal = Button(root, text= "Find Me A Meal!", bg="#1eff00",borderwidth=5, command = GetMeal)
button_exit = Button(root, text="Exit", padx=8.3, borderwidth=2, bg="#000000", fg="#ffffff", command=root.quit)


# Creating Drop Down Menus
meat = StringVar()
veg1 = StringVar()
veg2 = StringVar()
meat.set("Pork")
veg1.set("Corn")
veg2.set("Pasta")

meat_drop = OptionMenu(root, meat, "Pork", "Beef", "Chicken")
veg1_drop = OptionMenu(root, veg1, "Corn", "Spinach", "GreenBeans")
veg2_drop = OptionMenu(root, veg2, "Pasta", "Rice", "Potatoes")



#Putting buttons, labels, and menus into a grid
info_label.grid(row=0, columnspan=6, pady=5, padx=10)
meat_drop.grid(row=1, column=0, pady= 10, padx=10)
veg1_drop.grid(row=2, column=0, pady=10, padx=10)
veg2_drop.grid(row=3, column=0, pady=10, padx=10)
about.grid(row=4, column=5, padx=20, pady=20)
f_meal.grid(row=6, column=0, columnspan=6, padx=50)
button_exit.grid(row=5, column=5, pady=20)


root.mainloop()
