import tkinter as tk
import ttkbootstrap as ttk

class buttony:
    def __init__(self, master, text, command):
        self._master = master
        self._text = text
        self._command = command
# TODO : setters and getters

    def get_master(self):
       return self.__master
    def get_text(self):
       return self.__text
    def get_command(self):
       return self.__command
    def set_master(self):
        self.master = master_entry

    def use_button_function(self):
        aList.append(entry.get())
        print(aList)
        label['text'] = aList

aList = []

def button_function():

    aList.append(entry.get())
    print(aList)

    # if (label['text'] == aList):
    #     label['text'] = 'test'
    # else:
    label['text'] = aList

    # List is the main data structure used to store a mutable (changeable) sequence of elements -- elements do not need to be of the same type
    # One-dimensional writable data structure

    # List indexing
    # bin_colors = ['red', 'green', 'blue', 'yellow']
    # i = 0

    # for color in bin_colors:
    #     print(bin_colors[i])
    #     i = i + 1


def list_length():
    label2['text'] = len(aList)

def delete_tool():
   aList.pop()
   label['text'] = aList

def slicer():
   n = n_entry.get()
   m = m_entry.get()

   if not n:
      m = int(m_entry.get())
      label['text'] = aList[:m]
   elif not m:
      n = int(n_entry.get())
      label['text'] = aList[n:]
   else:
      n = int(n)
      m = int(m)
      label['text'] = aList[n:m]

def list_range():
   # TODO: create function
   x_entry = int(x_entry.get())
   aList = range(0, x_entry)
   label['text'] = aList


def search():
   aList.sort
   

   

#window
window = ttk.Window(themename= 'darkly', title='Test with Lists')

b = buttony(window, 'test', list_range)


#new frame
frame = ttk.Frame(master=window)
label = ttk.Label(master=frame)
label.pack()
frame.pack()

#entry
entry = ttk.Entry(master=frame)
label2 = ttk.Label(master=frame)
entry.pack()
label2.pack()


#button frame
button_frame = ttk.Frame(master=frame)
button_frame.pack(pady=5)

#buttons
button = ttk.Button(master=button_frame, text='Add and Display', style='w.tbutton', command=button_function)
button.pack(side='left', padx=3)

button2 = ttk.Button(master=button_frame, text='Length', command=list_length)
button2.pack(side='left', padx=3)

button3 = ttk.Button(master=button_frame, text='Delete', command=delete_tool)
button3.pack(side='left', padx=3)


#slice frame
slice_frame = ttk.Frame(master=frame)
n_entry = ttk.Entry(master=slice_frame)
m_entry = ttk.Entry(master=slice_frame)
button4 = ttk.Button(master=slice_frame, text='Slicer', command=slicer)
n_entry.pack(side='left', padx=3)
m_entry.pack(side='left', padx=3)
button4.pack(side='left', padx=3)
slice_frame.pack(pady=3)

# TODO: finish list frame
#list frame
list_frame = ttk.Frame(master=frame)
x_entry = ttk.Entry(master=list_frame)
button5 = ttk.Button(master=list_frame, text='List Filter', command=list_range)
x_entry.pack(side='left', padx=3)
button5.pack(side='left', padx=3)
list_frame.pack(pady=3)


class_master = ttk.Frame(master=frame)
master_entry = ttk.Entry(master=class_master)
text_entry = ttk.Entry(master=class_master)
command_entry = ttk.Entry(master=class_master)
master_entry.pack(side='left')
text_entry.pack(side='left')
command_entry.pack(side='left')
class_master.pack()

b2 = buttony(class_master, 'BAHHUMBUG', button_function)

print(b2._master, b2.get_text, b2.get_command)

buttontest = ttk.Button(master=b._master, text=b._text, command=b._command)
buttontest.pack(pady=3)


buttontest2 = ttk.Button(master=(b2._master), text=b2._text, command=b2._command)
buttontest2.pack(side='left')
print(b2._master)
#run
window.mainloop()