from tkinter import *

root = Tk()
root.geometry(str(240)+'x'+str(320) + '+' + str(150) + '+' + str(200))
root.title("Style" + "Demo")
root.configure(**{'background':'#'+'4D'*3})
root.option_readfile('OptionDB.txt')

Text(**dict(zip('background  foreground borderwidth relief width height master'.split(),
f'#{str(10)*3} #{"D6"*3} 18 sunken 16 5'.split() + [root])))

root.winfo_children()[0].insert(END,
"Style is Knowing\nwho you are, what\nyou want to say,\nand not giving a \ndamn")
root.winfo_children()[0].grid(row=0, column=0, columnspan=6, 
**{'padx':5, 'pady':5}, sticky=EW)

text_list_join = list(zip('text'.split()*9, '* ^ # < OK > + v -'.split()))

[
Button(**{'master':root}, **dict([text_list_join[(i+j)-1 if i == 0 else (i+j+2)-1 if i==1 else (i+j+4)-1 ]])).grid(row=i+1, column=j, sticky=EW) for i in range(0, 3) for j in range(1, 4)
]

[
Button(root, text=str(i)).grid(column=3 if i%3==0 else (1 if i%3==1 else 2),
row= 4 if i <= 3 else (5 if i<= 6 else 6), sticky=EW) for i in range(0, 10, 1)
]

root.mainloop()
