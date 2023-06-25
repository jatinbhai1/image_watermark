import tkinter as tk
from tkinter import messagebox

import PIL.Image
import ttkbootstrap as ttk
# importing the library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib.pyplot as plt
import numpy as np

from ttkbootstrap import Style
from tkinter import ttk
from tkinter import filedialog, END
root = tk.Tk()
root.title("Image Watermarking app")
root.config(bg='#ffffff')
root.geometry('1200x900')

FILE_PATH = ""
style = Style()
style.theme_use('flatly')
def change_theme(selected):

    theme_slected = myCombo.get()
    if theme_slected==themes_list[0]:
        root.config(bg='#ffffff')
        name_label.config(bg='#ffffff', fg='black')
        watermark_label.config(bg='#ffffff', fg='black')
        file_lbl.config(bg='#ffffff', fg='black')
        scale_label.config(bg='#ffffff', fg='black')
        scaler_lbl.config(bg='#ffffff', fg='black')

    elif theme_slected== themes_list[1]:
        root.config(bg='#213555')
        name_label.config(bg="#213555", fg='white')
        watermark_label.config(bg="#213555", fg='#F86F03')
        file_lbl.config(bg="#213555", fg='#F86F03')
        scale_label.config(bg="#213555", fg='#F86F03')
        scaler_lbl.config(bg="#213555", fg='#F86F03')


    elif theme_slected == themes_list[2]:
        root.config(bg='#9BCDD2')
        name_label.config(bg='#9BCDD2',fg='grey')
        watermark_label.config(bg='#9BCDD2',fg='grey')
        file_lbl.config(bg='#9BCDD2',fg='grey')
        scale_label.config(bg='#9BCDD2',fg='grey')
        scaler_lbl.config(bg='#9BCDD2',fg='grey')



def select_file():
    global FILE_PATH
    file_path = filedialog.askopenfilename(filetypes=[("Image File",'.jpg .png .jpeg')])
    FILE_PATH=file_path
    if file_path:
        browse_btn.config(text='Selected')

def clear_selected_file():
    global FILE_PATH
    FILE_PATH=""
    browse_btn.config(text='Browse')

def scaler_label(e):
    scaler_lbl.config(text=angle_scale.get().__floor__())
def adding_watermark_to_img():
    if len(FILE_PATH)==0:
        messagebox.showerror(title="Can't Process", message='Please select a image to procedd further')
    elif len(entry_box.get())==0:
        messagebox.showerror(title="Can't Process", message='Please type data to add watermark')
    else:
        image = Image.open(fp=FILE_PATH)

        watermark_image = image.copy()
        draw = ImageDraw.Draw(watermark_image)
        w, h = image.size
        x,y = int(w/2), int(h/2)
        if x>y:
            font_size = y
        if y>x:
            font_size=x
        else:
            font_size=x
        font = ImageFont.truetype('arial.ttf', int(font_size/6))
        draw.text((x,y), entry_box.get(), fill=(0,0,0), font=font, anchor='ms')
        plt.imshow(watermark_image)


def clear_all():
    entry_box.delete(0, END)
    clear_selected_file()
    angle_scale.set(0)
#here describing the strucutre of the app

themes_list = ['White', 'Dark', 'light']
myCombo = ttk.Combobox(root, values=themes_list)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", change_theme)
myCombo.place(x=1000,y=10)

#adding app nambe label
name_label = tk.Label(text='Add Watermark\nto Image', font=('cursive', 35, 'bold'), highlightthickness=0 )
name_label.place(x=400, y=50)

#adding a entry box having watermark naem
watermark_label = tk.Label(text='Enter data you want as watermark: ', font=('Arial', 14, 'bold'), pady=10, highlightthickness=0)
watermark_label.place(x= 300, y=240)
entry_box = ttk.Entry(root, width=50)
entry_box.place(x=300, y=280)

#adding a scale to get the angel
scale_label = tk.Label(text='Select angle to rotate watermark', highlightthickness=0,font=('Arial', 14, 'bold'))
scale_label.place(x=300, y=330)
angle_scale=ttk.Scale(root, orient='horizontal', bootstyle='warning', length=400,from_=0, to=180, command=scaler_label)
angle_scale.place(x=300, y=360)

scaler_lbl = tk.Label(text=0, highlightthickness=0, font=('Arial', 14, 'bold'))
scaler_lbl.place(x=730, y=355)
#adding add file
file_lbl = tk.Label(text='Add file', highlightthickness=0, font=('Arial', 14, 'bold'))

file_lbl.place(x=300, y=400)
browse_btn = ttk.Button(text='Browse', style='primary.TButton', width=15, command=select_file)
style.configure('primary.TButton', font=('Arial', 20))
browse_btn.config(padding=15)
browse_btn.place(x=300, y=430)

clear_browse_btn = tk.Button(text='X', command=clear_selected_file)
clear_browse_btn.place(x=580, y=450)

ok_btn = ttk.Button(text='Done',command=adding_watermark_to_img, style='success.TButton', width=15)
style.configure('success.TButton', background='green', font=('Arial', 16))
ok_btn.place(x=240, y=540)

cancel_btn = ttk.Button(text='Cancel', style='secondary.TButton', width=15, command=clear_all)
style.configure('secondary.TButton', background='red', font=('Arial', 16))
cancel_btn.place(x=560, y=540)


root.mainloop()