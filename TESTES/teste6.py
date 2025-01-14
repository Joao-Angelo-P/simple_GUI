# Remake the code from "Tkinter-By-Example- To-Do LIST v1" first part
from tkinter import *

class Todo(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("To-Do App v1")
        self.geometry(str(300)+"x"+str(400))

        Label(**dict(list(zip(
            ' text bg fg pady master'.split(),
            ['--- Add Items Here ---'] + 'lightgrey black 10'.split() + [self])))).pack(
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
            Label(self, text=text_task, pady=10)
            self.winfo_children()[-1].configure(**[{"bg":"black", "fg":"lightgrey"},
                                                   {"bg":"lightgrey", "fg":"black"}][
                                                       0 if (len(self.winfo_children())-1) % 2 == 0 else 1])

            self.winfo_children()[len(self.winfo_children())-1].pack(side=TOP, fill=X)

        self.winfo_children()[1].delete(1., END)


if __name__ == '__main__':
    app = Todo()
    app.mainloop()
