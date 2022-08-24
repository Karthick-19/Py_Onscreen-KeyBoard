import clipboard
from tkinter import *
import tkinter as tk

b = tk.Tk()
b.configure(bg="lightgreen")
b.geometry("1000x400")
b.title("Mouse-Keyboard")
b.maxsize(1000, 400)
b.minsize(1000, 400)

screen = Entry(b, width=150, borderwidth=3)
screen.place(x=50, y=80)

#############METHODS#######################


def copy():
    c = screen.get()
    op = clipboard.copy(c)


def clear():
    a = screen.get()
    screen.delete(0, "end")


def escape():
    b.quit()


def backspace():
    a = screen.get()
    screen.delete(first=len(a)-1, last="end")


def caps():
    con = screen.get()
    con.capitalize()


def enter():
    e = clipboard.paste()
    screen.insert(0, e)

#########################BACKGROUND COLORS#####################


def red_color():
    b.configure(bg="red")


def green_color():
    b.configure(bg="green")


def blue_color():
    b.configure(bg="blue")


def gray_color():
    b.configure(bg="gray")


def magenta_color():
    b.configure(bg="magenta")


def cyan_color():
    b.configure(bg="cyan")


def pink_color():
    b.configure(bg="pink")


def orange_color():
    b.configure(bg="orange")


esc = Button(b, text="esc", width=2, bg="gray", padx=10,
             relief=RIDGE, command=escape)
esc.grid(row=1, column=1, sticky="e", padx=10, pady=130)

symbol1 = Button(b, text="~", width=1, bg="silver", fg="magenta", padx=10,
                 pady=5, relief=RIDGE, command=lambda: screen.insert("end", "~"))
symbol1.grid(row=1, column=2, sticky="e", pady=130)

num1s = Button(b, text="!", bg="silver", fg="magenta", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "!"))
num1s.grid(row=1, column=3, sticky="e", padx=1, pady=130)

num2s = Button(b, text="@", bg="silver", fg="magenta", padx=7,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "@"))
num2s.grid(row=1, column=4, sticky="e", padx=1, pady=130)

num3s = Button(b, text="#", bg="silver", fg="magenta", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "#"))
num3s.grid(row=1, column=5, sticky="e", padx=1, pady=130)

num4s = Button(b, text="$", bg="silver", fg="magenta", padx=7,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "$"))
num4s.grid(row=1, column=6, sticky="e", padx=1, pady=130)

num5s = Button(b, text="%", bg="silver", fg="magenta", padx=7,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "%"))
num5s.grid(row=1, column=7, sticky="e", padx=1, pady=130)

num6s = Button(b, text="^", bg="silver", fg="magenta", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "^"))
num6s.grid(row=1, column=8, sticky="e", padx=1, pady=130)

num7s = Button(b, text="&", bg="silver", fg="magenta", padx=7,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "&"))
num7s.grid(row=1, column=9, sticky="e", padx=1, pady=130)

num8s = Button(b, text="*", bg="silver", fg="magenta", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "*"))
num8s.grid(row=1, column=10, sticky="e", padx=1, pady=130)

num9s = Button(b, text="(", bg="silver", fg="magenta", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "("))
num9s.grid(row=1, column=11, sticky="e", padx=1, pady=130)

num9s = Button(b, text=")", bg="silver", fg="magenta", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", ")"))
num9s.grid(row=1, column=12, sticky="e", padx=1, pady=130)

symbol2 = Button(b, text="_", width=1, bg="silver", fg="magenta", padx=10,
                 pady=5, relief=RIDGE, command=lambda: screen.insert("end", "_"))
symbol2.grid(row=1, column=13, sticky="e", padx=1, pady=130)

symbol3 = Button(b, text="+", width=1, bg="silver", fg="magenta", padx=10,
                 pady=5, relief=RIDGE, command=lambda: screen.insert("end", "+"))
symbol3.grid(row=1, column=14, sticky="e", padx=1, pady=130)

bs_button = Button(b, text="<-backspace", bg="gray", fg="red", activebackground="red", activeforeground="gray",
                   padx=2, pady=5, relief=RIDGE, command=backspace)
bs_button.grid(row=1, column=15, padx=5, pady=130)
############################ROW 2##############################################
tab = Button(b, text="tab|<-", bg="silver", fg="red", padx=4, pady=5, activebackground="red", activeforeground="silver",
             relief=RIDGE, command=lambda: screen.insert("end", "    "))
tab.place(x=10, y=170)

key_Q = Button(b, text="Q", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "q"))
key_Q.place(x=67, y=170)

key_W = Button(b, text="W", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "w"))
key_W.place(x=110, y=170)

key_E = Button(b, text="E", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "e"))
key_E.place(x=155, y=170)

key_R = Button(b, text="R", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "r"))
key_R.place(x=195, y=170)

key_T = Button(b, text="T", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "t"))
key_T.place(x=235, y=170)

key_Y = Button(b, text="Y", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "y"))
key_Y.place(x=275, y=170)

key_U = Button(b, text="U", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "u"))
key_U.place(x=315, y=170)

key_I = Button(b, text="I", bg="silver", fg="blue", padx=12,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "i"))
key_I.place(x=355, y=170)

key_O = Button(b, text="O", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "o"))
key_O.place(x=395, y=170)

key_P = Button(b, text="P", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "p"))
key_P.place(x=437, y=170)

curly = Button(b, text="{""}", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "{""}"))
curly.place(x=477, y=170)

symbol4 = Button(b, text="|", bg="silver", fg="blue", padx=10,
                 pady=5, relief=RIDGE, command=lambda: screen.insert("end", "|"))
symbol4.place(x=517, y=170)

front_slash = Button(b, text="\*", bg="silver", fg="blue", padx=10,
                     pady=5, relief=RIDGE, command=lambda: screen.insert("end", "\*"))
front_slash.place(x=557, y=170)
######################### ROW 3##################################
caps_lock = Button(b, text="CAPS", bg="gray", fg="white", activebackground="white", activeforeground="gray",
                   padx=15, pady=5, relief=RIDGE, command=caps)
caps_lock.place(x=10, y=210)

key_A = Button(b, text="A", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "a"))
key_A.place(x=83, y=210)

key_S = Button(b, text="S", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "s"))
key_S.place(x=125, y=210)

key_D = Button(b, text="D", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "d"))
key_D.place(x=165, y=210)

key_F = Button(b, text="F", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "f"))
key_F.place(x=205, y=210)

key_G = Button(b, text="G", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "g"))
key_G.place(x=245, y=210)

key_H = Button(b, text="H", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "h"))
key_H.place(x=285, y=210)

key_J = Button(b, text="J", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "j"))
key_J.place(x=325, y=210)

key_K = Button(b, text="K", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "k"))
key_K.place(x=365, y=210)

key_L = Button(b, text="L", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "l"))
key_L.place(x=405, y=210)

symbol5 = Button(b, text=":", bg="silver", fg="blue", padx=10,
                 pady=5, relief=RIDGE, command=lambda: screen.insert("end", ":"))
symbol5.place(x=445, y=210)

symbol6 = Button(b, text='"', bg="silver", fg="blue", padx=10,
                 pady=5, relief=RIDGE, command=lambda: screen.insert("end", '"'))
symbol6.place(x=485, y=210)

enter = Button(b, text="<---enter", bg="gray",
               fg="cyan", activebackground="cyan", activeforeground="gray", padx=12, pady=5, relief=RIDGE, command=enter)
enter.place(x=525, y=210)
#######################Row 4####################################
shift_clear = Button(b, text="Delete", bg="gray", fg="red", activebackground="red", activeforeground="gray",
                     padx=25, pady=5, relief=RIDGE, command=clear)
shift_clear.place(x=10, y=250)

key_Z = Button(b, text="Z", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "z"))
key_Z.place(x=105, y=250)

key_X = Button(b, text="X", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "x"))
key_X.place(x=145, y=250)

key_C = Button(b, text="C", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "c"))
key_C.place(x=185, y=250)

key_V = Button(b, text="V", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "v"))
key_V.place(x=225, y=250)

key_B = Button(b, text="B", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "b"))
key_B.place(x=265, y=250)

key_N = Button(b, text="N", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "n"))
key_N.place(x=305, y=250)

key_M = Button(b, text="M", bg="silver", fg="blue", padx=10,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", "m"))
key_M.place(x=345, y=250)

symbol7 = Button(b, text="<", bg="silver", fg="blue", padx=10,
                 pady=5, relief=RIDGE, command=lambda: screen.insert("end", "<"))
symbol7.place(x=390, y=250)

symbol8 = Button(b, text=">", bg="silver", fg="blue", padx=10,
                 pady=5, relief=RIDGE, command=lambda: screen.insert("end", ">"))
symbol8.place(x=430, y=250)

symbol9 = Button(b, text="?", bg="silver", fg="blue", padx=10,
                 pady=5, relief=RIDGE, command=lambda: screen.insert("end", "?"))
symbol9.place(x=470, y=250)

shift_copy = Button(b, text="CC", bg="gray", fg="red", activebackground="red", activeforeground="gray",
                    padx=30, pady=5, relief=RIDGE, command=copy)
shift_copy.place(x=510, y=250)
#################NUM SECTION#############################
num_7 = Button(b, text="7", bg="silver", fg="green", activebackground="green", activeforeground="silver",
               padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "7"))
num_7.place(x=620, y=130)

num_8 = Button(b, text="8", bg="silver", fg="green", activebackground="green", activeforeground="silver",
               padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "8"))
num_8.place(x=660, y=130)

num_9 = Button(b, text="9", bg="silver", fg="green", activebackground="green", activeforeground="silver",
               padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "9"))
num_9.place(x=700, y=130)

num_4 = Button(b, text="4", bg="silver", fg="green", activebackground="green", activeforeground="silver",
               padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "4"))
num_4.place(x=620, y=170)

num_5 = Button(b, text="5", bg="silver", fg="green", activebackground="green", activeforeground="silver",
               padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "5"))
num_5.place(x=660, y=170)

num_6 = Button(b, text="6", bg="silver", fg="green", activebackground="green", activeforeground="silver",
               padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "6"))
num_6.place(x=700, y=170)

num_1 = Button(b, text="1", bg="silver", fg="green", activebackground="green", activeforeground="silver",
               padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "1"))
num_1.place(x=620, y=210)

num_2 = Button(b, text="2", bg="silver", fg="green", activebackground="green", activeforeground="silver",
               padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "2"))
num_2.place(x=660, y=210)

num_3 = Button(b, text="3", bg="silver", fg="green", activebackground="green", activeforeground="silver",
               padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "3"))
num_3.place(x=700, y=210)

num_0 = Button(b, text="0", bg="silver", fg="green", activebackground="green", activeforeground="silver",
               padx=30, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "0"))
num_0.place(x=620, y=250)

sym_dot = Button(b, text=".", bg="silver", fg="green", activebackground="green", activeforeground="silver",
                 padx=12, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "."))
sym_dot.place(x=700, y=250)
###########################SPECIAL SYMBOLS##############################
spl_sym1 = Button(b, text="-", bg="silver", fg="black", activebackground="black", activeforeground="silver",
                  padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "-"))
spl_sym1.place(x=760, y=130)

spl_sym2 = Button(b, text="=", bg="silver", fg="black", activebackground="black", activeforeground="silver",
                  padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "="))
spl_sym2.place(x=800, y=130)

spl_sym3 = Button(b, text="/", bg="silver", fg="black", activebackground="black", activeforeground="silver",
                  padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", "/"))
spl_sym3.place(x=840, y=130)

spl_sym4 = Button(b, text=";", bg="silver", fg="black", activebackground="black", activeforeground="silver",
                  padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", ";"))
spl_sym4.place(x=880, y=130)

spl_sym5 = Button(b, text=",", bg="silver", fg="black", activebackground="black", activeforeground="silver",
                  padx=10, pady=5, relief=RIDGE, command=lambda: screen.insert("end", ","))
spl_sym5.place(x=920, y=130)
###########################BACKGROUND COLORS#############################
label_title = Label(b, text="Background Colors",
                    bg="black", fg="yellow", padx=44, pady=3)
label_title.place(x=760, y=180)

red_color = Button(b, text="", bg="red", activebackground="black",
                   padx=15, pady=5, command=red_color)
red_color.place(x=760, y=210)

green_color = Button(b, text="", bg="green", activebackground="black",
                     padx=15, pady=5, command=green_color)
green_color.place(x=810, y=210)

blue_color = Button(b, text="", bg="blue", activebackground="black",
                    padx=15, pady=5, command=blue_color)
blue_color.place(x=860, y=210)

gray_color = Button(b, text="", bg="gray", activebackground="black",
                    padx=15, pady=5, command=gray_color)
gray_color.place(x=910, y=210)

magenta_color = Button(b, text="", bg="magenta", activebackground="black",
                       padx=15, pady=5, command=magenta_color)
magenta_color.place(x=760, y=260)

cyan_color = Button(b, text="", bg="cyan", activebackground="black",
                    padx=15, pady=5, command=cyan_color)
cyan_color.place(x=810, y=260)

pink_color = Button(b, text="", bg="pink", activebackground="black",
                    padx=15, pady=5, command=pink_color)
pink_color.place(x=860, y=260)

orange_color = Button(b, text="", bg="orange", activebackground="black",
                      padx=15, pady=5, command=orange_color)
orange_color.place(x=910, y=260)
###################space bar#########################
space = Button(b, text="SPACE_BAR", bg="silver", fg="blue", padx=65,
               pady=5, relief=RIDGE, command=lambda: screen.insert("end", " "))
space.place(x=185, y=290)

b.mainloop()
