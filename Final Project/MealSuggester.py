from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Meal Suggester")
#root.iconbitmap('icons8-food-50.ico')



button_randm = Button(root, text="click", command=root.quit)
button_randm.pack()
button_exit = Button(root, text="Exit", command=root.quit); button_exit.pack()

my_img = ImageTk.PhotoImage(Image.open("images/RoughDraftLayout.jpg"))
my_label = Label(image=my_img)
my_label.pack()



root.mainloop()