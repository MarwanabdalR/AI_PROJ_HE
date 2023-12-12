from tkinter import *

def easy():

    pass

def medium():
    pass

def difficult():
    pass

root = Tk()
root.geometry("850x500")
root.title("Tic Tac Toe 4*4*4")
btn1 = Button(root, text="Easy", command=easy,width=15, height=2, font=( 50), fg="black", padx=5, pady=5)
btn1.pack()
btn2 = Button(root, text="Medium", command=medium, width=15, height=2, font=(50), bg="black", fg="white", padx=5, pady=5)
btn2.pack()
btn3 = Button(root, text="Defficult", command=difficult, width=15, height=2, font=( 50), bg="black", fg="white", padx=5, pady=5)
btn3.pack()




# For maltie button
def start():
    pass

root.mainloop()