from tkinter import *
form =Tk()

form.geometry("800x600")

canvas =Canvas(form, width =700,height =600)
canvas.pack()
img = PhotoImage(file = "gif")

canvas.create_image(0 ,0 ,image =img.jpg ,anchor = NW)
form.mainloop()


