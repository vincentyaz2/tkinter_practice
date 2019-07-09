'''
Following tutorial of Jomar Malate @ https://www.youtube.com/watch?v=JrWHyqonGj8

Covered: 
-simple gui building
-insert entry fields, labels
-insert buttons
-displaying results 

'''

import tkinter as tk

# window has all the properties of tk
window = tk.Tk()

window.title('My App')
window.geometry('400x400')

# arguments/documentation can be found in effbot.org/tkinterbook

# label
title = tk.Label(text='Hello World', font=('Times New Roman', 20))
title.grid(column = 0, row = 0)

# button
button1 = tk.Button(text='Click me!', bg = 'red')
button1.grid(column = 0, row = 1)

# entry field
entry_field = tk.Entry()
entry_field.grid(column = 0, row = 2)

# text field
text_field = tk.Text(master=window, heigh=5, width=15)
text_field.grid(column = 0, row = 3)


# mainloop runs everything inside that window
window.mainloop()





























