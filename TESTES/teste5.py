from tkinter import *

root = Tk()
root.geometry("240x320+150+200")
root.title("Style Demo")
root.configure(background="#4D4D4D")
root.option_readfile('OptionDB.txt')

Text(root, background='#101010', foreground='#D6D6D6', borderwidth='18', relief='sunken', width='16', height='5')

root.winfo_children()[0].insert(END,
"Style is Knowing\nwho you are, what\nyou want to say,\nand not giving a \ndamn")
root.winfo_children()[0].grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky=EW)

Button(root, text='*').grid(row=1, column=1, sticky=EW)
Button(root, text='^').grid(row=1, column=2, sticky=EW)
Button(root, text='#').grid(row=1, column=3, sticky=EW)
Button(root, text='<').grid(row=2, column=1, sticky=EW)
Button(root, text='OK').grid(row=2, column=2, sticky=EW)
Button(root, text='>').grid(row=2, column=3, sticky=EW)
Button(root, text='+').grid(row=3, column=1, sticky=EW)
Button(root, text='v').grid(row=3, column=2, sticky=EW)
Button(root, text='-').grid(row=3, column=3, sticky=EW)

Button(root, text='1').grid(row=4, column=1, sticky=EW)
Button(root, text='2').grid(row=4, column=2, sticky=EW)
Button(root, text='3').grid(row=4, column=3, sticky=EW)
Button(root, text='4').grid(row=5, column=1, sticky=EW)
Button(root, text='5').grid(row=5, column=2, sticky=EW)
Button(root, text='6').grid(row=5, column=3, sticky=EW)
Button(root, text='7').grid(row=6, column=1, sticky=EW)
Button(root, text='8').grid(row=6, column=2, sticky=EW)
Button(root, text='9').grid(row=6, column=3, sticky=EW)

root.mainloop()
