
from tkinter import *
import random
from random_team import Random_Team_Func

window = Tk()
window.title("隨機分組程式.py")
window.minsize(width=500, height=500)
window.resizable(width=True, height=True)

label1 = Label(text = "number of people", font = ("Arial", 10, "bold") , height = 1, padx = 5, pady = 5)
label1.place(x = 5, y = 50)
Np_spinbox1 = Spinbox(from_ = 0, to = 100, font = ("Arial", 14, "bold"), width = 5)
Np_spinbox1.place(x = 140, y = 50)

label2 = Label(text = "number of teams", font = ("Arial", 10, "bold") , height = 1, padx = 5, pady = 5)
label2.place(x = 5, y = 100)
Nt_spinbox2 = Spinbox(from_ = 0, to = 100, font = ("Arial", 14, "bold"), width = 5)
Nt_spinbox2.place(x = 140, y = 100)

names = Text(font = ("Arial", 14, "bold"), width = 20, height = 10)
names.place(x = 5, y = 150)

outlabel = Label(text = "",font = ("Arial", 14, "bold"), padx = 5, pady = 5)
outlabel.place(x = 250, y = 100)


def Btn_click():
    N = Np_spinbox1.get()
    teams = Nt_spinbox2.get()
    names_list = []
    tmp = names.get("1.0", END).split(sep= "\n")
    for i in range(int(N)):
        names_list.append(tmp[i])
    print(N, teams)
    print(names_list)
    team = Random_Team_Func(int(N), int(teams), names_list)
    print(team)
    txt = ""
    for i in range(len(team)):
        txt += "The " + str(i+1) +  " th team:\n"
        for j in range(len(team[i])):
            txt += str(team[i][j]) + "\n"

    outlabel.config(text = txt)
    return 0
Btn = Button(text = "開始分組", font = ("Arial", 14, "bold"), padx = 5, pady = 5, command=Btn_click)
Btn.place(x = 50, y = 400)
window.mainloop()





