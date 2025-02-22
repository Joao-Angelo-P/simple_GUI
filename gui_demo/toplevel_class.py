#from ex2.Login import verificar
from tkinter import Label, Toplevel, Tk, Button, Entry
from os import getenv
from sys import platform

class App(Toplevel): # nome vai ser "Login"

    
    def __init__(self, master=None, *rags, **kw):
        super(App, self).__init__(master)
        self.master = master
        self.master.withdraw()
        self.title("Janela")
        self.geometry("200x200")
        self.so()


    def widgets(self):
        [x.destroy() for x in self.winfo_children()]
        self.geometry('180x90')
        #self.limpar
        Label(self, text="Usuario").grid(row=0, column=0)
        Label(self, text="Senha:").grid(row=1, column=0)
        Entry(self).grid(row=0, column=1)
        Entry(self).grid(row=1, column=1)
        Button(self, text="--Entrar--", command=lambda:self.sair()).grid(row=2, column=1)

    def sair(self, event=None, var=False):
        self.withdraw()
        if len(self.master.winfo_children()) == 1:
            Label(master=self.master, text="Acesso Negado\nAperte no botao 'sair' pra fechar o sistema\nEssa é uma janela Toplevel.").pack()
            Button(master=self.master, text="Voltar",
                command=lambda: [x() for x in (self.master.withdraw, self.deiconify)]).pack()
            Button(master=self.master, text="Destruir",
                command=lambda: self.master.destroy()).pack()
            
        self.master.deiconify()
        self.master.title("Master")

    def validar(self):
        if self.winfo_children()[1].get() == getenv("usuario") and self.winfo_children()[3].get() == getenv("senha"):
            self.sair()

    def so(self):
        if (resposta:=self.verificacao()):
            self.widgets()

        else:
            
            Label(master=self, **{'text':'Seu Sistema Operacional é windows, \nfavor configurar as variaveis de ambiente\n "usuario" e "senha"'}, font='Verdana 18 bold').grid(row=0, column=0)
            Button(master=self, text="ok", command=self.widgets, width="5", font="bold 12").grid(row=1, column=0)
            self.geometry('600x200')

    def verificacao(self):
        return True if platform in ('linux', 'darwin') else False

master = Tk()
app = App(master)
master.mainloop()
