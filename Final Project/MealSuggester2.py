from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Meal Suggester")
root.iconbitmap('icons8-food-50.ico')
root.configure(background="#524c4c")
root.geometry("350x400+500+500")
root.resizable(width=False, height=False)

#Creating buttons
menu_reset = Button(root, text="Reset", padx=3., bg="#000000", fg="#ffffff")
f_meal = Button(root, text= "Find Me A Meal!", bg="#1eff00",borderwidth=5)
button_exit = Button(root, text="Exit", padx=8.3, borderwidth=2, bg="#000000", fg="#ffffff", command=root.quit)
blank=Label(root, text="")

#Putting buttons into a grid
blank.grid(row=0, column=1, columnspan=2, pady=130)
menu_reset.grid(row=1, column=2, padx=2, pady=20)
f_meal.grid(row=2, column=1, padx=95)
button_exit.grid(row=2, column=2)


# my_img = ImageTk.PhotoImage(Image.open("images/RoughDraftLayout.jpg"))
# my_label = Label(image=my_img)
# my_label.pack()



root.mainloop()