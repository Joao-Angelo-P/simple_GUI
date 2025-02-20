# 0 "/mnt/d/1_2025_ubuntu/fevereiro/gui_demo/gui_demo.py"
# 0 "<built-in>"
# 0 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 0 "<command-line>" 2
# 1 "/mnt/d/1_2025_ubuntu/fevereiro/gui_demo/gui_demo.py"
import tkinter as tk
import tkinter.constants as CONS
from os import getenv

class Login(tk.Tk):
    def __init__(self, *args, **kw):

        super(Login, self).__init__(*args, **kw)
        self.title("Janela")
        self.createWindow()


    def createWindow(self):

        tk.Label(master=self, text="Login:",)
        tk.Entry(master=self,)
        tk.Label(master=self, text="Senha:")
        tk.Entry(master=self, show="*")
        tk.Button(master=self, text="Logar", command=self.logado)


    def exibir(self):

        self.winfo_children()[0].grid(row=0, column=0)
        self.winfo_children()[1].grid(row=0, column=1)
        self.winfo_children()[2].grid(row=1, column=0)
        self.winfo_children()[3].grid(row=1, column=1)
        self.winfo_children()[4].grid(row=2, column=1, pady=(2, 0))

        if not (resposta:=self.verificacao()):

            index_wdg = slice(-1, -3, -1)
            [x.destroy() for x in self.winfo_children()[index_wdg]]
            self.geometry('220x70')

    def __call__(self):
        if (resposta:=self.verificacao()):
            self.exibir()

        else:
            tk.Label(master=self, **{'text':'Seu Sistema Operacional é windows, \nfavor configurar as variaveis de ambiente\n "usuario" e "senha"'}, font='Verdana 18 bold').grid(row=0, column=0)
            tk.Button(self, text="ok", command=self.exibir, width="5", font="bold 12").grid(row=1, column=0)


        self.mainloop()

    def logado(self, event=None):

        if self.winfo_children()[1].get() == getenv("usuario") and self.winfo_children()[3].get() == getenv("senha"):

            self.withdraw()
            self.top = tk.Toplevel()

            tk.Label(master=self.top, text="Bem-Vindo").pack()
            tk.Button(self.top, text="Voltar", command=self.voltar).pack()
            self.top.geometry("300x300")
            self.top.title("App v1.0.1")


        else:

            self.geometry("200x200")

            self.withdraw()
            self.top = tk.Toplevel()
            self.top.title('Janela')
            self.top.geometry('230x100')
            tk.Label(master=self.top, text="Acesso Negado\nAperte no botao 'sair' pra fechar o sistema\nEssa é uma janela Toplevel.").pack(anchor=CONS.CENTER)
            tk.Button(self.top, text="Voltar", command=self.voltar).pack()
            tk.Button(self.top, text="Sair", command=lambda: self.destroy() ).pack()


    def voltar(self, event=None):

        self.top.withdraw()
        self.deiconify()


    @staticmethod
    def verificar():

        import sys
        print("E linux") if sys.platform in ('linux', 'darwin') else print("E windows")

    def verificacao(self):

        import sys
        return True if sys.platform in ('linux', 'darwin') else False



if __name__ == '__main__':

    app = Login()
    app.verificar()
    app()
