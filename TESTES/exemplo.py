# exemplo copiado mas um pouco modificado do livro 'Tkinter-By-Example'
import tkinter as tk

conf_tasks_text = {
                   "side":tk.TOP,
                   "fill": tk.X
                   }
color = [
    {"bg":"grey", "fg":"lightgrey"},
    {"bg":"lightgrey", "fg":"grey"}
]

class APP(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        self.var_text = tk.StringVar()
        self.tasks = [] if tasks is None else tasks

        self.title("TODO App v1")
        self.geometry("400x300")
        self["bg"] = "black"
        self.label_1 = tk.Label(self, text="Primeiro Texto...", font=("Bold", 14), bg="grey", fg="lightgrey")
        self.textarea = tk.Text(self,
                                height=3)

        self.tasks.append(self.label_1)

        for x in self.tasks:
            x.pack(**conf_tasks_text)
            #print(x)

        self.textarea.pack(side=tk.BOTTOM, fill=tk.X)
        #self.label_1.pack(side=tk.TOP, fill=tk.X)

        self.textarea.focus_set()

        self.bind('<Return>', self.add_task)

    def add_task(self, event=None):
        get_text = self.textarea.get(1., tk.END).strip()
        if len(get_text) > 0:
            t_label = tk.Label(self, text=get_text, **color[0 if len(self.tasks) % 2 == 0 else 1], pady=10)
            self.tasks.append(t_label)
            t_label.pack(**conf_tasks_text)

        #print(len(self.tasks))
        #print(get_text + ' | ' + str(len(get_text)))
        self.textarea.delete(1., tk.END)





if __name__ == '__main__':
    app = APP()
    app.mainloop()

