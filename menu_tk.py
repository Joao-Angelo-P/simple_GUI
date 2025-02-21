import tkinter as tk
from typing import Optional, Union



def inserir(top):
    top.destroy()
    tk.Label(master=root, text=f"---\t{texto.get()} {len(root.winfo_children())}\t---").pack()

def modificar(top):
    top.destroy()
    try:
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
[tk.Label(master=root, text=f"---\tTexto Qualquer {i}\t---").pack() for i in range(1, 4, 1)]



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
