import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        l = tk.Label(self, text="Login:")
        l2 = tk.Label(self, text="Senha:")

        self.en = tk.Entry(self,)
        self.en2 = tk.Entry(self,)

        btn = tk.Button(self, text="Entrar", command=self.login)
        l.grid(row=0, column=0, columnspan=1, pady=5)
        self.en.grid(row=0, column=1,pady=5)
        l2.grid(row=1, column=0, columnspan=1)
        self.en2.grid(row=1, column=1)
        btn.grid(row=2, column=3)

        # Configuração da Janela
        self.geometry("500x500")
        self.title("Janela")

    def login(self):
        s1, s2 = (self.en.get(), self.en2.get())
        if s1 == 'admin' and s2 == 'admin':
            wn = tk.Toplevel(self)

            l = tk.Label(wn, text="Bem-Vindo").pack()
            wn.title("Nova Janela")
            wn.geometry("300x250")
        else:
            wn = tk.Toplevel(self)
            l = tk.Label(wn, text="Acesso Negado", ).pack()
            wn.title("Negado")
            wn.geometry("300x300")

if __name__ == '__main__':
    app = App()
    app.mainloop()