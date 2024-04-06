from tkinter import *
from tkinter.ttk import *
from tkinter import font, colorchooser
from PIL import Image, ImageTk

class TextEditor:
    def __init__(self, root, text_frame):
        self.root = root
        self.text_frame = text_frame
        self.fontSize = 12
        self.fontStyle = 'Arial'

        def font_style(event=None):
            self.fontStyle = 'Arial'
            self.fontStyle = font_family_variable.get()
            text_input.config(font=(self.fontStyle, self.fontSize))

        def font_size(event=None):
            self.fontSize = 12
            self.fontSize = size_variable.get()
            text_input.config(font=(self.fontStyle, self.fontSize))


        def bold_text():
            text_property = font.Font(font=text_input['font']).actual()
            if text_property['weight'] == 'normal':
                text_input.config(font=(self.fontStyle, self.fontSize, 'bold'))
            elif text_property['weight'] == 'bold':
                text_input.config(font=(self.fontStyle, self.fontSize, 'normal'))

        def italic_text():
            text_property = font.Font(font=text_input['font']).actual()
            if text_property['slant'] == 'roman':
                text_input.config(font=(self.fontStyle, self.fontSize, 'italic'))
            elif text_property['slant'] == 'italic':
                text_input.config(font=(self.fontStyle, self.fontSize, 'roman'))

        def underline_text():
            text_property = font.Font(font=text_input['font']).actual()
            if text_property['underline'] == 0:
                text_input.config(font=(self.fontStyle, self.fontSize, 'underline'))
            elif text_property['underline'] == 1:
                text_input.config(font=(self.fontStyle, self.fontSize, 'normal'))

        def color_select():
            color = colorchooser.askcolor()
            text_input.config(fg=color[1])

        def align_right():
            text_input.tag_config('right', justify=RIGHT)
            text_input.tag_add('right', '1.0', END)

        def align_left():
            text_input.tag_config('left', justify=LEFT)
            text_input.tag_add('left', '1.0', END)

        def align_center():
            text_input.tag_config('center', justify=CENTER)
            text_input.tag_add('center', '1.0', END)

        root = Tk()
        root.title("備忘錄")
        root.geometry("1200x620+10+10")
        root.resizable(False, False)

        labelframe = LabelFrame(root, width=400, height=50, text='標題')
        labelframe.pack(padx=10, pady=10)
        input_font = ("Helvetica", 20)

        text_area = Text(labelframe, width=400, height=1, wrap='none', font=input_font)
        text_area.pack()

        tool_bar = Label(root)
        tool_bar.pack(side=TOP, fill=X)
        font_families = font.families()
        font_family_variable = StringVar()
        fontfamily_Combobox = Combobox(tool_bar, width=30, value=font_families, state='readonly',
                                       textvariable=font_family_variable)
        fontfamily_Combobox.current(font_families.index('Arial'))
        fontfamily_Combobox.grid(row=0, column=0, padx=13)
        size_variable = IntVar()
        font_size_Combobox = Combobox(tool_bar, width=14, textvariable=size_variable, state='readonly',
                                      values=tuple(range(8, 81)))
        font_size_Combobox.current(4)
        font_size_Combobox.grid(row=0, column=1, padx=5)

        fontfamily_Combobox.bind('<<ComboboxSelected>>', font_style)
        font_size_Combobox.bind('<<ComboboxSelected>>', font_size)

        # apply_font_sizeImage = PhotoImage(file='icon/tick.png')
        # apply_font_size_button = Button(tool_bar, image=apply_font_sizeImage, command=font_size)
        # apply_font_size_button.grid(row=0, column=2, padx=5)

        bold_image = Image.open('icon/bold.png')
        self.bold_icon = ImageTk.PhotoImage(bold_image)
        boldButton = Button(tool_bar, image=self.bold_icon, command=bold_text)
        boldButton.grid(row=0, column=3, padx=5)

        italic_image = Image.open('icon/italic.png')
        self.italic_icon = ImageTk.PhotoImage(italic_image)
        italicButton = Button(tool_bar, image=self.italic_icon, command=italic_text)
        italicButton.grid(row=0, column=4, padx=5)

        underline_image = Image.open('icon/underline.png')
        self.underline_icon = ImageTk.PhotoImage(underline_image)
        underlineButton = Button(tool_bar, image=self.underline_icon, command=underline_text)
        underlineButton.grid(row=0, column=5, padx=5)

        font_color_image = Image.open('icon/font_Color.png')
        self.font_color_icon = ImageTk.PhotoImage(font_color_image)
        fontColorButton = Button(tool_bar, image=self.font_color_icon, command=color_select)
        fontColorButton.grid(row=0, column=6, padx=5)

        left_align_image = Image.open('icon/left.png')
        self.left_align_icon = ImageTk.PhotoImage(left_align_image)
        leftAlignButton = Button(tool_bar, image=self.left_align_icon, command=align_left)
        leftAlignButton.grid(row=0, column=7, padx=5)

        right_align_image = Image.open('icon/right.png')
        self.right_align_icon = ImageTk.PhotoImage(right_align_image)
        rightAlignButton = Button(tool_bar, image=self.right_align_icon, command=align_right)
        rightAlignButton.grid(row=0, column=8, padx=5)

        center_align_image = Image.open('icon/center.png')
        self.center_align_icon = ImageTk.PhotoImage(center_align_image) 
        centerAlignButton = Button(tool_bar, image=self.center_align_icon, command=align_center)
        centerAlignButton.grid(row=0, column=9, padx=5)

        labelframe = LabelFrame(root, width=400, height=150, text='內容')
        labelframe.pack(padx=10, pady=5)

        text_input = Text(labelframe, width=400, height=150, wrap='word')
        text_input.pack(fill=BOTH, expand=True)

        #root.mainloop()

# Create an instance of the TextEditor class to run the application
#editor = TextEditor()
