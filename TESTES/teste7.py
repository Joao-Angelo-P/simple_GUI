# Remake the code from "Tkinter-By-Example- To-Do LIST v1" second part
# https://github.com/Dvlv/Tkinter-By-Example/blob/master/Code/Chapter2-2.py

from tkinter import *
from tkinter.messagebox import askyesno
from verticalscrolledframe import VerticalScrolledFrame as vsf

class Todo(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("To-Do App v2")
        self.geometry(str(300)+"x"+str(400))
        vsf(self, height=200, width=250).pack(fill=BOTH, expand=1)
        
        Label(**dict(list(zip(
            ' text bg fg pady master'.split(),
            ['--- Add Items Here ---'] + 'lightgrey black 10'.split() + [[x for x in self.winfo_children() if isinstance(x, Frame)][0].interior])))).pack(
                **{'side':TOP,
                   'fill':BOTH})

        Text(**{'master':self},
             cnf={'height':'3', 'bg':'white', 'fg':'black'})
        
        self.winfo_children()[1].pack(side=BOTTOM, fill=X)
        self.winfo_children()[1].focus_set()
        self.bind('<Return>', self.add_task)

    def add_task(self, event=None):
        text_task = self.winfo_children()[1].get("1.0", END).strip()
        if len(text_task) > 0:
            Label([x for x in self.winfo_children() if isinstance(x, Frame)][0].interior,
                  text=text_task, pady=10).pack(side=TOP, fill=X)
            
            [x for x in self.winfo_children() if isinstance(x, Frame)][0].interior.winfo_children()[-1].configure(**[{"bg":"black", "fg":"lightgrey"},
                                                   {"bg":"lightgrey", "fg":"black"}][
                                                       1 if (len([x for x in self.winfo_children() if isinstance(x, Frame)][0].interior.winfo_children())-1) % 2 == 0 else 0])
            
            [x for x in self.winfo_children() if isinstance(x, Frame)][0].interior.winfo_children()[-1].bind("<Button-1>", self.remove_task)
        self.winfo_children()[1].delete(1., END)


    def remove_task(self, event):
        widget = event.widget
        if askyesno("Really Delete?", "Delete " + widget.cget("text") + "?"):
            event.widget.destroy()
            
            for i in [x for x in self.winfo_children() if isinstance(x, Frame)][0].interior.winfo_children():
                i.configure(**[{"bg":"black", "fg":"lightgrey"},
                                                   {"bg":"lightgrey", "fg":"black"}][
                                                       1 if ([x for x in self.winfo_children() if isinstance(x, Frame)][0].interior.winfo_children().index(i)) % 2 == 0 else 0])

if __name__ == '__main__':
    app = Todo()
    app.mainloop()
