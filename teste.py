import tkinter as tk
from os import getenv

class Login(tk.Tk):
    def __init__(self, *args, **kw):
        super(Login, self).__init__(*args, **kw)

        self.title("Janela")
    
        self.createWindow()
        self.logado()

    def createWindow(self):
        tk.Label(master=self, text="Login:",)
        tk.Entry(master=self,)
        tk.Label(master=self, text="Senha:")
        tk.Entry(master=self, show="*")
        tk.Button(master=self, text="Logar", command=self.logado)

    def __call__(self):
        self.winfo_children()[0].grid(row=0, column=0)
        self.winfo_children()[1].grid(row=0, column=1)
        self.winfo_children()[2].grid(row=1, column=0)
        self.winfo_children()[3].grid(row=1, column=1)
        self.winfo_children()[4].grid(row=2, column=1)

        
        self.mainloop()

    def logado(self, event=None):
        
        if self.winfo_children()[1].get() == getenv("usuario") and self.winfo_children()[3].get() == getenv("senha"):
            print("logado")
            



if __name__ == '__main__':
    app = Login()
    app()

	
