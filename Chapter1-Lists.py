import tkinter as tk
import ttkbootstrap as ttk

aList = []

def button_function():

    aList.append(entry.get())
    print(aList)

    if (label['text'] == aList):
        label['text'] = 'test'
    else:
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
    print(len(aList))

def delete_tool():
   aList.pop()
   print(aList)
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
   

#window
window = ttk.Window(title='Test with Lists')

#new frame
frame = ttk.Frame(master=window)
label = ttk.Label(master=frame)
label.pack()
frame.pack()

#entry
entry = ttk.Entry(master=frame)
entry.pack(pady=5)

#button frame
button_frame = ttk.Frame(master=frame)
button_frame.pack(pady=5)

#buttons
button = ttk.Button(master=button_frame, text='Add and Display', command=button_function)
button.pack(side='left', padx=3)

button2 = ttk.Button(master=button_frame, text='Length', command=list_length)
button2.pack(side='left', padx=3)

button3 = ttk.Button(master=button_frame, text='Delete', command=delete_tool)
button3.pack(side='left', padx=3)


#slice frame
slice_frame = ttk.Frame(master=frame)
n_entry = ttk.Entry(master=slice_frame)
m_entry = ttk.Entry(master=slice_frame)
button4 = ttk.Button(master=slice_frame, text='Button 4', command=slicer)
n_entry.pack(side='left', padx=3)
m_entry.pack(side='left', padx=3)
button4.pack(side='left', padx=3)
slice_frame.pack(pady=3)

#run
window.mainloop()