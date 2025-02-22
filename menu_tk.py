import tkinter as tk
from typing import Optional


# implementar extração de dados e
# apresentar como estar em baixo
# Usando um match pattern para filtrar objeto

data_ = [
    ('Cereal SUCRILHOS', 'UN',12.99),
    ('ACHOC. PRONTO TODDYNHO', 'UN',3.19),
    ('ACHOC. PRONTO TODDYNHO', 'UN',3.19),
    ('SALGADO FOLHADO DE QUEIJO', 'KG',41.90),
    ('PAO DE QUEIJO', 'KG', 29.90),
    ('PAO FRANCES', 'KG',9.99),
    ('LEITE UHT INTEGRAL', 'UN', 7.69),
    ('BOLO DE MARACUJÁ','KG', 34.90),
    ('QUEIJO MUSSARELA', 'KG', 62.90),
    ('MELAO AMARELO', 'KG', 9.99),
    ('PAO BRIOCHE', 'KG', 17.90),
    ('ABACAXI GRANDE', 'KG', 12.99),
    ('Item inavalido exemplo', 'X', 2.33),
    ]

# Filtro com match stetement
def itens_extraidos():
    for j in [Item(*i) for i in data_]:
        match j:
            case Item(nome=nome, kg_ou_un='KG', unidade_valor=valor):
                print(f'Este item tem quantidade pelo KILO\n{nome}\tR${valor:,}')

            case Item(nome=nome, kg_ou_un='UN', unidade_valor=valor):
                print(f'Este item tem quantidade pelo UNIDADE\n{nome}\tR${valor:,}')

            case _:
                print(f'Entrada Invalida')
            

class Item(NamedTuple):
    nome:str
    kg_ou_un:str
    unidade_valor:float

# Dados ja dentro da classe builder
db_objects = [Item(*i) for i in data_]


def inserir(top):
    top.destroy()
    tk.Label(master=root, text=f"---\t{texto.get()} {len(root.winfo_children())}\t---").pack()

def modificar(top):
    top.destroy()
    try:
        if int(index.get()):
            x1 = [i  for i in root.winfo_children() if i.__class__.__name__=='Label']
            #var = x1[index.get()]
            x1[index.get()-1]["text"] = texto.get()

    except IndexError:
        #print('Passou na exceção')
        top2 = tk.Toplevel()
        tk.Label(master=top2,
                 text='Voce inseriu um numero maior que não contem na lista',
                 font="Verdana 18 bold").pack()
        tk.Button(master=top2, text="Ciente!", command=lambda: top2.destroy()).pack(anchor="CENTER".lower())

def apagar(top):
    top.destroy()
    try:
        if int(index.get()):
            x1 = [i  for i in root.winfo_children() if i.__class__.__name__=='Label']
            x1[index.get()-1].destroy()
            
    except IndexError:
        #print('Passou na exceção')
        top2 = tk.Toplevel()
        tk.Label(master=top2,
                 text='Voce inseriu um numero maior que não contem na lista',
                 font="Verdana 18 bold").pack()
        tk.Button(master=top2, text="Ciente!", command=lambda: top2.destroy()).pack(anchor="CENTER".lower())

def filefunc(event: Optional[object] = None):
    ''' Nada Implantado '''
    #print(f'Entrada da opção: "File"')
    top = tk.Toplevel()
    tk.Label(master=top, text="Qual o texto do novo item?").pack()
    tk.Entry(top, textvar=texto).pack()
    #tk.Label(master=root, text=f"---\t{texto.get()} {len(root.winfo_children()) + 1}\t---").pack()
    tk.Button(master=top, text="Inserir", command=lambda: inserir(top)).pack()
    

def editfunc(event: Optional[object] = None):
    ''' Nada Implantado '''
    #print(f'Entrada da opção: "Edit"')
    top = tk.Toplevel()
    tk.Label(master=top, text="Qual numero do item?").pack()
    tk.Entry(top, textvar=index).pack()
    tk.Label(master=top, text="Qual novo texto?").pack()
    tk.Entry(top, textvar=texto).pack()
    #tk.Label(master=root, text=f"---\t{texto.get()} {len(root.winfo_children()) + 1}\t---").pack()
    tk.Button(master=top, text="Modificar", command=lambda: modificar(top)).pack()

def formatfunc(event: Optional[object] = None):
    ''' Nada Implantado '''
    #print(f'Entrada da opção: "Format"')
    top = tk.Toplevel()
    tk.Label(master=top, text="Qual numero do item que quer apagar?").pack()
    tk.Entry(top, textvar=index).pack()
    tk.Button(master=top, text="Apagar", command=lambda: apagar(top)).pack()

# Root widgets    
root = tk.Tk()
root.geometry("300x200")
root.title("Menu Tkinter")
texto = tk.StringVar()
index = tk.IntVar()
menubar = tk.Menu(master=root)

#[tk.Label(master=root, text=f"---\tTexto Qualquer {i}\t---").pack() for i in range(1, 4, 1)]
tk.Label(master=root, text="Nome do Item\t|\tKG OU UN\t|\tValor").pack()
[tk.Label(master=root, text=f"{j.nome}\t|\t{j.kg_ou_un}\t|\t{j.unidade_valor}").pack() for j in db_objects[:3]]


# Menu "File"
filemenu = tk.Menu(master=menubar, tearoff=False)
filemenu.add_command(**{
    'label':'Adicionar', 'command': lambda: filefunc()})

#menubar.add_cascade(**{'label':'File', 'menu':filemenu})


# Menu "Edit"
editmenu = tk.Menu(master=menubar, tearoff=False)
editmenu.add_command(**{'label':'Modificar',
                        'command': lambda: editfunc()})

# Menu "Format"
formatmenu = tk.Menu(master=menubar, tearoff=False)
formatmenu.add_command(label="Excluir", command=formatfunc)




menubar.add_cascade(menu=filemenu, label="File")
menubar.add_cascade(label='Edit', menu=editmenu)
menubar.add_cascade(label="Format", menu=formatmenu)
root.config(**{'menu':menubar})

'''
cont = 0
for x in root.winfo_children():
    if x.__class__.__name__ == 'Label':
        cont += 1
        print(f"{x.__class__.__name__ } n°{cont}")
'''


root.mainloop()
