import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
        def __init__(self, master=None):
                tk.Frame.__init__(self, master)#super().__init__(master)
                #self.labelframe()
                self.logo()
                self.createWidgtes()
                self.frameWidgets()
                self.grid()

        def createWidgtes(self):
                self.frameButton = tk.Frame(self)
                self.frameButton.grid(row=1, column=1, sticky='e')
                self.btn1 = ttk.Button(self.frameButton, text='Cancel')
                self.btn2 = ttk.Button(self.frameButton, text='Finish')

                
                self.btn1.pack(side=tk.LEFT, padx=(0, 5))#self.btn1.grid(row=1, column=1, sticky='e')
                self.btn2.pack(side=tk.RIGHT)#self.btn2.grid(row=1, column=2,  sticky='e', padx=(0, 10))

        def labelframe(self): #não está sendo usada
                self.lf = tk.LabelFrame(self, text='Electrum Wallet', width=500, height=500, padx=5, pady=5)
                self.lf.grid(row=0, column=1)
                
                texto = tk.Label(self.lf, text='Wallet:', bg="grey")
                texto.grid(row=0, column=0, sticky='w')

                entrada = tk.Entry(self.lf,)
                entrada.grid(row=0, column=1, sticky='w')
                
                botao = tk.Button(self.lf, text='Choose...')
                botao.grid(row=0, column=2)

                texto2 = tk.Label(self.lf, text='This file is encrypted with a passoword.' +
                                  '\nEnter your password or choose another file.',
                                  )
                texto2.grid(row=1, column=0)

        def frameWidgets(self):
                self.fp = tk.Frame(self, borderwidth=1, relief="solid", height=400, width=600)
                self.fp.grid(row=0, column=1, pady=10)

                #tk.Label(self.fp, text='TESTE').pack()
                self.linha1_h = tk.Frame(self.fp,  #bg="lightgrey"
                                         ) 
                label1 = tk.Label(self.fp, text='Electrum wallet',
                                  font=('Arial', 9, 'bold'))
                
                label2 = tk.Label(self.linha1_h, text='Wallet:',)
                entry1 = ttk.Entry(self.linha1_h,)
                b1 = ttk.Button(self.linha1_h, text='Choose...')
                
                label3 = tk.Label(self.fp, text='This file is encrypted with a passoword.' +
                                  '\nEnter your password or choose another file.',
                                  justify=tk.LEFT) #justify=tk.LEFT
                #Frame para Label->"Password" & Entry
                self.pass_e_entry = tk.Frame(self.fp, #bg="lightgrey"
                                             )
                label4 = tk.Label(self.pass_e_entry, text='Password:')
                entry2 = ttk.Entry(self.pass_e_entry)
                
                label5 = tk.Label(self.fp, text='Alternatively:')
                b2 = ttk.Button(self.fp, text='Create New Walltet')

                label1.grid(row=0, column=0,  sticky='w')
#Frame_3.grid(row=2, column=0)

                self.linha1_h.grid(row=1, column=0, sticky='nswe', padx=(10, 0))
                label2.grid(row=0, column=0)
                entry1.grid(row=0, column=3, columnspan=3)
                b1.grid(row=0, column=7, pady=3, sticky='e', padx=(0, 10))

                
                label3.grid(row=2, column=0, pady=(20, 20))

                #
                self.pass_e_entry.grid(row=3, column=0, sticky='nswe', padx=(10, 0))
                label4.grid(row=0, column=0)
                entry2.grid(row=0, column=1)
                
                label5.grid(row=4, column=0, sticky='w', padx=(10, 0), pady=(20, 0)
                            )
                b2.grid(row=5, column=0, sticky='w', padx=(10, 0), pady=(0, 10))


                
        def logo(self):
                self.logo = tk.PhotoImage(file='./electrum_darkblue_1.png')
                tk.Label(self, image=self.logo).grid(row=0, column=0, sticky='N', pady=10)

app = Application()
app.master.title('Create/Restore Wallet')
app.master.geometry('600x650')
app.mainloop()
