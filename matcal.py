from tkinter import *
import numpy as np


def show_createmat():
    global root, scr, urow, ucol, stage
    fixedmat_btn = Button(root, text="Fixed Matrix Size", command=dummy)
    dynamicmat_btn = Button(root, text="Dynamic Matrix Size", command=dummy)
    pastemat_btn = Button(root, text="Paste Matrix", command=dummy)
    back_btn = Button(root, text="Back", command=lambda: transit("main"))
    scr.append(fixedmat_btn)
    scr.append(dynamicmat_btn)
    scr.append(pastemat_btn)
    scr.append(back_btn)
    for i in scr:
        i.grid(row=mr(), column=ucol)


def show_welcome():
    global root, scr, urow, ucol, stage
    hilabel = Label(root, text="Welcome to matrix calculator")
    creatorlabel = Label(root, text="created by Naphat and Samita")
    matter_btn = Button(root, text="Create Matrix",
                        command=lambda: transit("createmat"))
    hilabel.grid(row=urow, column=ucol)
    creatorlabel.grid(row=mr(), column=ucol)
    matter_btn.grid(row=mr(), column=ucol)
    scr.append(hilabel)
    scr.append(creatorlabel)
    scr.append(matter_btn)


def dummy():
    print("hello debug...")


def clearer():
    global root, scr, urow, ucol, stage
    for i in scr:
        i.grid_forget()
    scr = []
    urow = 0
    ucol = 0


def mr():
    global root, scr, urow, ucol, stage
    urow += 1
    return urow


def mc():
    global root, scr, urow, ucol, stage
    ucol += 1
    return ucol


def def_btn():
    global root, scr, urow, ucol, stage
    rem = Button(root, text="clear", command=clearer)
    summ = Button(root, text="refresh", command=summon)
    # summ.grid(row=mr(), column=ucol)
    # rem.grid(row=urow, column=mc())


def transit(news):
    global stage
    stage = news
    clearer()
    summon()


def summon():
    global stage
    if stage == "main":
        show_welcome()
    elif stage == "createmat":
        show_createmat()


if __name__ == '__main__':
    root = Tk()
    scr = []
    allmat = []
    urow = 0
    ucol = 0
    stage = "main"
    summon()
    def_btn()

    root.mainloop()
