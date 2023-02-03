from tkinter import *
import numpy as np


def show_fixedmat():
    global root, scr, urow, ucol, stage, asset
    row_lab = Label(root, text="Number of Row: ")
    col_lab = Label(root, text="Number of Column: ")
    row_ent = Entry(root, width=5)
    col_ent = Entry(root, width=5)
    next_btn = Button(root, text="Next",
                      command=lambda: next1_fixedmat(row_ent, col_ent))
    back_btn = Button(root, text="Back", command=lambda: transit("createmat"))
    home_btn = Button(root, text="Home", command=lambda: transit("main"))
    scr.append(back_btn)
    scr.append(row_lab)
    scr.append(col_lab)
    scr.append(row_ent)
    scr.append(col_ent)
    scr.append(next_btn)
    scr.append(home_btn)
    row_lab.grid(row=urow, column=ucol)
    row_ent.grid(row=urow, column=ucol+1)
    col_lab.grid(row=mr(), column=ucol)
    col_ent.grid(row=urow, column=ucol+1)
    next_btn.grid(row=mr(), column=ucol)
    back_btn.grid(row=mr(), column=ucol)
    home_btn.grid(row=mr(), column=ucol)


def next1_fixedmat(re, ce):
    global root, scr, urow, ucol, stage, asset
    err = ""
    if re.get().isdigit() and ce.get().isdigit():
        r = int(re.get())
        c = int(ce.get())
        if r <= 0 or c <= 0:
            err = "cannot be lower than 1"

    else:
        err = "not digit"
    if err == "":
        asset["fixedmat_r"] = r
        asset["fixedmat_c"] = c
        # transit("fixedmat2")
        transit("main")
    else:
        re.delete(0, END)
        ce.delete(0, END)
        print("show msg box err")


def show_createmat():
    global root, scr, urow, ucol, stage, asset
    fixedmat_btn = Button(root, text="Fixed Matrix Size",
                          command=lambda: transit("fixedmat"))
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
    global root, scr, urow, ucol, stage, asset
    hilabel = Label(root, text="Welcome to matrix calculator")
    creatorlabel = Label(root, text="created by Naphat and Samita")
    matter_btn = Button(root, text="Create Matrix",
                        command=lambda: transit("createmat"))
    exit_btn = Button(root, text="Quit", command=exitProg)

    hilabel.grid(row=urow, column=ucol)
    creatorlabel.grid(row=mr(), column=ucol)
    matter_btn.grid(row=mr(), column=ucol)
    exit_btn.grid(row=mr(), column=ucol)
    scr.append(hilabel)
    scr.append(creatorlabel)
    scr.append(matter_btn)
    scr.append(exit_btn)


def exitProg():
    global root
    root.destroy()


def dummy():
    print("hello debug...")


def clearer():
    global root, scr, urow, ucol, stage, asset
    for i in scr:
        i.grid_forget()
    scr = []
    urow = 0
    ucol = 0


def mr():
    global root, scr, urow, ucol, stage, asset
    urow += 1
    return urow


def mc():
    global root, scr, urow, ucol, stage, asset
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
    elif stage == "fixedmat":
        show_fixedmat()


if __name__ == '__main__':
    root = Tk()
    scr = []
    allmat = []
    urow = 0
    ucol = 0
    asset = {}
    stage = "main"
    summon()
    def_btn()

    root.mainloop()
