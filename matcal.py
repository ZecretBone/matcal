from tkinter import *
from tkinter import messagebox
import numpy as np
import random


def beauty_mat(m):
    b = ""
    rc = m.shape
    r = rc[0]
    c = rc[1]
    # b = m
    # export matrix
    for i in range(r):
        for j in range(c):
            b += str(m[i, j]) + "  "
        b += "\n"
    return b


def disp_matlist(listb, lab):
    global root, scr, urow, ucol, stage, asset
    an = listb.get(ANCHOR)
    mat = None
    for i in range(len(asset["all_mat"])):
        if asset["all_mat"][i][0] == an:
            mat = asset["all_mat"][i][1]
    b = beauty_mat(mat)
    lab.config(text=b)


def random_fixedmat(all_ent):
    global root, scr, urow, ucol, stage, asset
    print("entries")
    for r, row in enumerate(all_ent):
        for c, entry in enumerate(row):
            newf = round(random.uniform(-100, 100), 2)
            entry.delete(0, END)
            entry.insert('end', str(newf))


def show_matlist():
    global root, scr, urow, ucol, stage, asset
    mat_lb = Listbox(root)
    mat_lab = Label(root, text="")
    mat_show = Button(root, text="Display",
                      command=lambda: disp_matlist(mat_lb, mat_lab))
    for i in range(len(asset["all_mat"])):
        print(asset["all_mat"][i][0])
        mat_lb.insert(END, asset["all_mat"][i][0])
    back_btn = Button(root, text="Back", command=lambda: transit("main"))
    mat_lb.grid(row=0, column=0)
    mat_show.grid(row=1, column=0)
    back_btn.grid(row=2, column=0)
    mat_lab.grid(row=3, column=0)
    scr.append(mat_lb)
    scr.append(back_btn)
    scr.append(mat_lab)
    scr.append(mat_show)


def validate_fixedmat(t):
    try:
        t = float(t)
        return t, ""
    except:
        return 0, "input invalid"


def namer_fixedmat(name):
    global root, scr, urow, ucol, stage, asset
    dup = False
    f = True
    while dup or f:
        f = False
        dup = False
        for i in range(len(asset["all_mat"])):
            if asset["all_mat"][i][0] == name:
                name += "_duplicate"
                dup = True
    return name


def save_fixedmat(all_ent, name):
    global root, scr, urow, ucol, stage, asset
    a = asset["fixedmat_arr"]
    have_err = False
    for r, row in enumerate(all_ent):
        for c, entry in enumerate(row):
            text = entry.get()
            print(text)
            a[r, c], err = validate_fixedmat(text)
            if err != "":
                have_err = True
    if have_err:
        messagebox.showerror(title="Create Matrix Error",
                             message="Invalid input, please re-enter your input")
    else:
        newname = namer_fixedmat(name.get())
        asset["all_mat"].append([newname, a])
        print(a)
        print(asset["all_mat"])
        transit("main")
        messagebox.showinfo(title="Create Matrix Success",
                            message="Your new matrix has been created !")


def show_fixedmat_two():
    global root, scr, urow, ucol, stage, asset
    arr = np.zeros((asset["fixedmat_r"],  asset["fixedmat_c"]))
    asset["fixedmat_arr"] = arr
    for c in range(asset["fixedmat_c"]):
        l = Label(root, text=str(c+1))
        l.grid(row=0, column=c+1)
        scr.append(l)
    all_ent = []
    for r in range(asset["fixedmat_r"]):
        ent_row = []
        l = Label(root, text=str(r+1))
        l.grid(row=r+1, column=0)
        scr.append(l)
        for c in range(asset["fixedmat_c"]):
            en = Entry(root, width=7)
            en.insert('end', 0)
            en.grid(row=r+1, column=c+1)
            ent_row.append(en)
            scr.append(en)
        all_ent.append(ent_row)
    name_lab = Label(root, text="Matrix Name: ")
    name_ent = Entry(root, width=7)
    save_btn = Button(root, text='Save',
                      command=lambda: save_fixedmat(all_ent, name_ent))
    random_btn = Button(root, text='Random',
                        command=lambda: random_fixedmat(all_ent))
    random_btn.grid(row=asset["fixedmat_r"]+1, column=0)
    name_lab.grid(row=asset["fixedmat_r"]+2, column=0)
    name_ent.grid(row=asset["fixedmat_r"]+2, column=1)
    save_btn.grid(row=asset["fixedmat_r"]+3, column=0)
    canc_btn = Button(root, text='Cancel', command=lambda: transit("main"))
    canc_btn.grid(row=asset["fixedmat_r"]+4, column=0)
    scr.append(canc_btn)
    scr.append(save_btn)
    scr.append(name_lab)
    scr.append(name_ent)
    scr.append(random_btn)


def show_matdisp():
    print("in progress")


def show_matfunc():
    print("in progress")


def show_fixedmat():
    global root, scr, urow, ucol, stage, asset
    root.title("Matrix Calculator: Create Fixed Matrix Size >> Define Size")
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
    root.title("Matrix Calculator: Create Fixed Matrix Size >> Define Element")
    err = ""
    if re.get().isdigit() and ce.get().isdigit():
        r = int(re.get())
        c = int(ce.get())
        if r <= 0 or c <= 0:
            err = "Input cannot be lower than 1"

    else:
        err = "Input has to be an integer"
    if err == "":
        asset["fixedmat_r"] = r
        asset["fixedmat_c"] = c
        # transit("fixedmat2")
        transit("fixedmat_two")
    else:
        re.delete(0, END)
        ce.delete(0, END)
        print("show msg box err")
        messagebox.showerror(title="Create Matrix Error", message=err)


def show_createmat():
    global root, scr, urow, ucol, stage, asset
    root.title("Matrix Calculator: Create Matrix")
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
    root.title("Matrix Calculator: Main Menu")
    root.geometry("500x500")
    hilabel = Label(root, text="Welcome to matrix calculator")
    creatorlabel = Label(root, text="created by Naphat and Samita")
    matter_btn = Button(root, text="Create Matrix",
                        command=lambda: transit("createmat"))
    matlist_btn = Button(root, text="Matrix List",
                         command=lambda: transit("matlist"))
    matfunc_btn = Button(root, text="Do Functions",
                         command=lambda: transit("matfunc"))
    exit_btn = Button(root, text="Quit", command=exitProg)

    hilabel.grid(row=urow, column=ucol)
    creatorlabel.grid(row=mr(), column=ucol)
    matter_btn.grid(row=mr(), column=ucol)
    matlist_btn.grid(row=mr(), column=ucol)
    matfunc_btn.grid(row=mr(), column=ucol)
    exit_btn.grid(row=mr(), column=ucol)
    scr.append(hilabel)
    scr.append(creatorlabel)
    scr.append(matter_btn)
    scr.append(exit_btn)
    scr.append(matlist_btn)
    scr.append(matfunc_btn)


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
    elif stage == "matlist":
        show_matlist()
    elif stage == "matfunc":
        show_matfunc()
    elif stage == "fixedmat_two":
        show_fixedmat_two()


if __name__ == '__main__':
    root = Tk()

    scr = []
    allmat = []
    urow = 0
    ucol = 0
    asset = {}
    asset["all_mat"] = []
    stage = "main"
    summon()
    def_btn()

    root.mainloop()
