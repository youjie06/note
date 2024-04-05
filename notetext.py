from tkinter import *
from tkinter.ttk import *
from tkinter import font,colorchooser

fontSize=12
fontStyle='arial'
def font_style():
    global fontStyle, fontSize
    fontStyle=font_family_variable.get()
    text_input.config(font=(fontStyle, fontSize))

def font_size():
    global fontSize
    fontSize=size_variable.get()
    text_input.config(font=(fontStyle, fontSize))
    
    
def bold_text():
    text_property=font.Font(font=text_input['font']).actual()
    if text_property['weight']=='normal':
        text_input.config(font=(fontStyle,fontSize,'bold'))
        
    if text_property['weight']=='bold':
        text_input.config(font=(fontStyle,fontSize,'bold'))

def italic_text():
    text_property=font.Font(font=text_input['font']).actual()
    if text_property['slant']=='roman':
        text_input.config(font=(fontStyle,fontSize,'italic'))
        
    if text_property['slant']=='italic':
        text_input.config(font=(fontStyle,fontSize,'roman'))

def underline_text():
    text_property=font.Font(font=text_input['font']).actual()
    if text_property['underline']==0:
        text_input.config(font=(fontStyle,fontSize,'underline'))
        
    if text_property['underline']==1:
        text_input.config(font=(fontStyle,fontSize))

def color_select():
    color=colorchooser.askcolor()
    text_input.config(fg=color[1])

def align_right():
    data=text_input.get(0.0,END)
    text_input.tag_config('right',justify=RIGHT)
    text_input.delete(0.0,END)
    text_input.insert(INSERT,data,'right')
    
def align_left():
    data=text_input.get(0.0,END)
    text_input.tag_config('left',justify=LEFT)
    text_input.delete(0.0,END)
    text_input.insert(INSERT,data,'left')
    
def align_center():
    data=text_input.get(0.0,END)
    text_input.tag_config('center',justify=CENTER)
    text_input.delete(0.0,END)
    text_input.insert(INSERT,data,'center')

root = Tk()
root.title("備忘錄")
root.geometry("1200x620+10+10")
root.resizable(False,False)

labelframe = LabelFrame(root, width=400, height=50, text='標題')
labelframe.pack(padx=10, pady=10)
input_font = ("Helvetica", 20)

text_area = Text(labelframe, width=400, height=1, wrap='none', font=input_font)
text_area.pack()

tool_bar=Label(root)
tool_bar.pack(side=TOP,fill=X)
font_families=font.families()
font_family_variable=StringVar()
fontfamily_Combobox=Combobox(tool_bar,width=30,value=font_families,state='readonly',textvariable=font_family_variable)
fontfamily_Combobox.current(font_families.index('Arial'))
fontfamily_Combobox.grid(row=0,column=0,padx=13)
size_variable=IntVar()
font_size_Combobox=Combobox(tool_bar, width=14, textvariable=size_variable,state='readonly',values=tuple(range(8,81 )))
font_size_Combobox.current(4)
font_size_Combobox.grid(row=0,column=1,padx=5)

fontfamily_Combobox.bind('<<ComboboxSelected>>',font_style)
fontfamily_Combobox.bind('<<ComboboxSelected>>',font_size)

apply_font_sizeImage=PhotoImage(file='icon/tick.png')
apply_font_size_button = Button(tool_bar,image=apply_font_sizeImage, command=font_size)
apply_font_size_button.grid(row=0, column=2, padx=5)

boldImage=PhotoImage(file='icon/bold.png')
boldButton=Button(tool_bar,image=boldImage,command=bold_text)
boldButton.grid(row=0,column=3,padx=5)

italicImage=PhotoImage(file='icon/italic.png')
italicButton=Button(tool_bar,image=italicImage,command=italic_text)
italicButton.grid(row=0,column=4,padx=5)

underlineImage=PhotoImage(file='icon/underline.png')
underlineButton=Button(tool_bar,image=underlineImage,command=underline_text)
underlineButton.grid(row=0,column=5,padx=5)

fontColorImage=PhotoImage(file='icon/font_Color.png')
fontColorButton=Button(tool_bar,image=fontColorImage,command=color_select)
fontColorButton.grid(row=0,column=6,padx=5)

leftAlignImage=PhotoImage(file='icon/left.png')
leftAlignButton=Button(tool_bar,image=leftAlignImage,command=align_left)
leftAlignButton.grid(row=0,column=7,padx=5)

rightAlignImage=PhotoImage(file='icon/right.png')
rightAlignButton=Button(tool_bar,image=rightAlignImage,command=align_right)
rightAlignButton.grid(row=0,column=8,padx=5)

centerAlignImage=PhotoImage(file='icon/center.png')
centerAlignButton=Button(tool_bar,image=centerAlignImage,command=align_center)
centerAlignButton.grid(row=0,column=9,padx=5)

labelframe = LabelFrame(root, width=400, height=150, text='內容')
labelframe.pack(padx=10, pady=5)

text_input = Text(labelframe, width=400, height=150, wrap='word')
text_input.pack(fill=BOTH,expand=True)

root.mainloop()