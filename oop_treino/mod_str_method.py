from tkinter import Tk, Label, Frame, Toplevel
from decostring import decolabel

class Label_ex(Label):
    def __init__(self, master, *args, **kw):
        super(Label_ex, self).__init__(master, *args, **kw)

    @decolabel
    def __str__(self):
        return super(Label_ex, self).__str__()

    def __repr__(self):
        return self.__str__()



master = Tk()
b = Toplevel(master)
f = Frame(b)
f.pack()
a = Label_ex(f, text="Widget")
a.pack()
print(a) # Tk(Parent) > Toplevel(Parent) > Frame(Parent) > Label_ex

master.destroy()
