from tkinter import Tk, Label, Entry
from collections import defaultdict

class TESTE(Tk):
    def __init__(self):
        super(TESTE, self).__init__()


    def winfo_children(self):
        objs = super(TESTE, self).winfo_children()
        d = defaultdict(list)
        for x in objs:
            d[x.__class__.__name__].append(x)

        Label(self, text=f"Sao {len(objs)} widgets\n'Label': {d['Label']}\n'Entry':{d['Entry']}").pack()

teste = TESTE()

Label(teste)
Label(teste)
Label(teste)
Entry(teste)
Entry(teste)
Entry(teste)

teste.winfo_children()
teste.mainloop()
