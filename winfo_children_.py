from tkinter import Tk, Label, Entry
from collections import defaultdict
from typing import get_type_hints

class TESTE(Tk):
    def __init__(self):
        super(TESTE, self).__init__()


    def winfo_children(self, _list: bool = None, _reverse: bool = True) -> dict | list:
        objs = super(TESTE, self).winfo_children()
        d = defaultdict(list)
        for x in objs:
            d[x.__class__.__name__].append(x)

        Label(self, text=f"Sao {len(objs)} widgets\n'Label': {d['Label']}\n'Entry':{d['Entry']}").pack()

        if _list:
            return sorted(d.items(), reverse=_reverse)

        else:
            return d


teste = TESTE()

Label(teste)
Label(teste)
Label(teste)
Entry(teste)
Entry(teste)
Entry(teste)

print(teste.winfo_children(True, False))
print(teste.winfo_children())
print(get_type_hints(teste.winfo_children))

teste.mainloop()
