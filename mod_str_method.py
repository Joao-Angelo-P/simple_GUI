from tkinter import Tk, Label, Frame, Toplevel

class Label_ex(Label):
    def __init__(self, master, *args, **kw):
        super(Label_ex, self).__init__(master, *args, **kw)

    def __str__(self):
        _str = super(Label_ex, self).__str__()

        sa = ''
        p = 'parent'
        
        for i in _str.split('.'):
            if not i:
                sa += f'Tk({str.capitalize(p)}) > '

            if i and i != _str.split('.')[-1]:
                sa += str.capitalize(f'{i[1:]}(') + str.capitalize(f'{p})')+ ' > '

            if i == _str.split('.')[-1]:
                sa += str.capitalize(f'{i[1:]}')
        return sa

    def __repr__(self):
        return self.__str__()
    
master = Tk()
b = Toplevel(master)
f = Frame(b)
f.pack()
a = Label_ex(f, text="Widget")
a.pack()
print(a) # .!toplevel.!frame.!label

master.destroy()
