from tkinter import *
from tkinter import messagebox
import numpy as np
import random
import pyperclip as pc
# from textwrap import wrap
from matfunc import *


def save_pastemat(cd, rd, ent, name):
    global root, scr, urow, ucol, stage, asset
    if name.get() == "":
        messagebox.showerror(title="Create Matrix Error",
                             message="Matrix name must not be empty")
        return
    e = ent.get("1.0", END)
    # e = ent.get()
    # print(e)
    try:
        newm = np.array(np.mat(e))
        print(newm)
        print(newm[1, 2])
        newname = namer_fixedmat(name.get())
        print(newname)
        asset["all_mat"].append([newname, newm])
        messagebox.showinfo(title="Create Matrix Success",
                            message="Your new matrix has been created !")
        transit("main")
    except:
        messagebox.showerror(title="Create Matrix Error",
                             message="Invalid input, please check your pasted text")
        return


def paste_pastemat(ent):
    global root, scr, urow, ucol, stage, asset
    if ent.get("1.0", END) != "":
        ent.delete("1.0", END)
    ent.insert('end', str(pc.paste()))


def show_pastemat():
    global root, scr, urow, ucol, stage, asset
    root.title("Matrix Calculator: Create Paste Matrix")
    cd = ","
    rd = ";"
    paste_ent = Text(root, width=30, height=10, bg="#EEEEEE")
    # paste_ent = Entry(root, width=30)
    name_ent = Entry(root, width=7)
    name_lab = Label(root, text="Matrix Name: ")
    save_btn = Button(root, text="Save",
                      command=lambda: save_pastemat(cd, rd, paste_ent, name_ent))
    home_btn = Button(root, text="Cancel",
                      command=lambda: transit("main"))
    paste_btn = Button(root, text="Paste",
                       command=lambda: paste_pastemat(paste_ent))
    paste_ent.grid(row=urow, column=ucol)
    paste_btn.grid(row=mr(), column=ucol)
    name_ent.grid(row=mr(), column=ucol)
    # name_ent.grid(row=urow, column=ucol)
    save_btn.grid(row=mr(), column=ucol)
    home_btn.grid(row=mr(), column=ucol)
    scr.append(paste_ent)
    scr.append(name_ent)
    scr.append(save_btn)
    scr.append(home_btn)
    scr.append(paste_btn)
    scr.append(name_lab)


def export_mat(m):
    b = "["
    rc = m.shape
    r = rc[0]
    c = rc[1]
    # b = m
    # export matrix
    for i in range(r):
        for j in range(c):
            b += str(m[i, j])
            if j != c-1:
                b += ","
        if i != r-1:
            b += ";"
    b += "]"
    return b


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


def disp_matlist(listb, lab, opt):
    global root, scr, urow, ucol, stage, asset
    an = listb.get(ANCHOR)
    mat = None
    if an != "":
        for i in range(len(asset["all_mat"])):
            if asset["all_mat"][i][0] == an:
                mat = asset["all_mat"][i][1]
        if opt == "export":
            b = export_mat(mat)
            pc.copy(b)
            messagebox.showinfo(title="Export Matrix Success",
                                message="Selected Matrix is copied to clipboard")
            print(len(mat))
            if len(mat) > 10:
                n = 100
                b = [b[i:i+n] for i in range(0, len(b), n)]
                print(b)
                b = '\n'.join(b)
                print("after join")
                # print(b)

        else:
            b = beauty_mat(mat)
        lab.config(text=b)
    else:
        messagebox.showerror(title="Display/Export Matrix Error",
                             message="Please select any matrix first")


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
    root.title("Matrix Calculator: Matrix List")
    mat_lb = Listbox(root)
    mat_lab = Label(root, text="")
    mat_show = Button(root, text="Display",
                      command=lambda: disp_matlist(mat_lb, mat_lab, "disp"))
    mat_export = Button(root, text="Export",
                        command=lambda: disp_matlist(mat_lb, mat_lab, "export"))
    for i in range(len(asset["all_mat"])):
        # print(asset["all_mat"][i][0])
        mat_lb.insert(END, asset["all_mat"][i][0])
    back_btn = Button(root, text="Back", command=lambda: transit("main"))
    mat_lb.grid(row=urow, column=0)
    mat_show.grid(row=mr(), column=0)
    mat_export.grid(row=mr(), column=0)
    back_btn.grid(row=mr(), column=0)
    mat_lab.grid(row=mr(), column=0)
    scr.append(mat_lb)
    scr.append(back_btn)
    scr.append(mat_lab)
    scr.append(mat_show)
    scr.append(mat_export)


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
            # print(text)
            a[r, c], err = validate_fixedmat(text)
            if err != "":
                have_err = True
    if have_err:
        messagebox.showerror(title="Create Matrix Error",
                             message="Invalid input, please re-enter your matrix input")
    else:
        newname = namer_fixedmat(name.get())
        if newname == "":
            messagebox.showerror(title="Create Matrix Error",
                                 message="Invalid input, Matrix name must not be empty")
            return
        asset["all_mat"].append([newname, a])
        # print(a)
        # print(asset["all_mat"])
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


def validate_matfunc(mat_lb):
    global root, scr, urow, ucol, stage, asset
    cm = mat_lb.get(ANCHOR)
    asset["current_matname"] = ""
    if cm == "":
        messagebox.showerror(title="Matrix Function Error",
                             message="Please select any matrix first")
        return
    for i in range(len(asset["all_mat"])):
        if asset["all_mat"][i][0] == cm:
            asset["current_matname"] = cm
            asset["current_mat"] = asset["all_mat"][i][1]
    if asset["current_matname"] != "":
        # transit("matfunc3")
        print("using func")
        if asset["current_func"] == "Elementary":
            print("elementary func..")
            transit("elementary")
    else:
        messagebox.showerror(title="Matrix Function Error",
                             message="Something went wrong")


def show_elementary2():
    global root, scr, urow, ucol, stage, asset
    root.title("Matrix Calculator: Functions >> Result (Elementary)")
    result = elemental(asset["current_mat"], asset["current_ans"])
    if not result["isconsist"]:
        return
    print("generating step and result")
    r = result["entire"]
    print("all r")
    print(r)
    onlye = []
    onlym = []
    onlyr = []
    j = 0

    for i in range(len(r)):
        nl = beauty_mat(r[i])
        nt = Label(root, text=nl)
        scr.append(nt)
        if j == 0:
            onlym.append(nt)
            j += 1
        elif j == 1:
            onlye.append(nt)
            j += 1
        else:
            onlyr.append(nt)
            j = 0
    for m in range(len(onlye)):
        onlye[m].grid(row=mr(), column=ucol)
        x_lab = Label(root, text="x")
        x_lab.grid(row=urow, column=mc())
        scr.append(x_lab)
        onlym[m].grid(row=urow, column=mc())
        next_lab = Label(root, text=">>")
        next_lab.grid(row=urow, column=mc())
        scr.append(next_lab)
        onlyr[m].grid(row=urow, column=mc())
        ucol = 0
    ns_lab = Label(root, text="NEXT STEP:")
    scr.append(ns_lab)
    ns_lab.grid(row=mr(), column=ucol)
    re = result["entire2"]
    jj = 0
    for k in range(len(re)):
        nl2 = beauty_mat(re[k])
        s2 = Label(root, text=nl2)
        scr.append(s2)
        if jj == 0:
            s2.grid(row=urow, column=mc())
            jj += 1
        elif jj == 1:
            x_lab = Label(root, text="x")
            next_lab = Label(root, text=">>")
            scr.append(x_lab)
            scr.append(next_lab)
            x_lab.grid(row=urow, column=mc())
            s2.grid(row=urow, column=mc())
            next_lab.grid(row=urow, column=mc())
            jj = 0
    print(result["firstans"])
    b_ans = beauty_mat(result["firstans"])
    b_lab = Label(root, text=b_ans)
    scr.append(b_lab)
    if result["togetans"] != []:
        ucol = 0
        x_lab = Label(root, text="x")
        next_lab = Label(root, text=">>")
        scr.append(x_lab)
        scr.append(next_lab)
        ns_lab2 = Label(root, text="GET NEW ANSWER SET:")
        scr.append(ns_lab2)
        ns_lab2.grid(row=mr(), column=ucol)
        r3 = beauty_mat(result["newans"])
        r3_lab = Label(root, text=r3)
        scr.append(r3_lab)
        nl2 = beauty_mat(re[-1])
        s2 = Label(root, text=nl2)
        scr.append(s2)
        s2.grid(row=urow, column=mc())
        x_lab.grid(row=urow, column=mc())
        b_lab.grid(row=urow, column=mc())
        next_lab.grid(row=urow, column=mc())
        r3_lab.grid(row=urow, column=mc())

    ivar_lab = Label(root, text="ALL VARIABLES: ")
    scr.append(ivar_lab)
    ucol = 0
    ivar_lab.grid(row=mr(), column=ucol)
    iv = len(result["var"])-1
    iiv = 1
    vt = ""
    while iv >= 0:
        vt += "x"+str(iiv)+" = "+str(result["var"][iv])
        if iv != 0:
            vt += ", "
        if len(vt) > 30:
            vt += "\n"
        iv -= 1
        iiv += 1
    var_lab = Label(root, text=vt)
    scr.append(var_lab)
    var_lab.grid(row=urow, column=mc())

    ucol = 0
    home_btn = Button(root, text="Home", command=lambda: transit("main"))
    scr.append(home_btn)
    home_btn.grid(row=mr(), column=ucol)

    # for i in range(len())
    # print(result)


def validate_elementary(all_ent):
    global root, scr, urow, ucol, stage, asset
    asset["current_ans"] = []
    er = False
    for i in all_ent:
        try:
            x = float(i.get())
            asset["current_ans"].append([x])
        except:
            er = True
    if er:
        messagebox.showerror(title="Matrix Function Error",
                             message="Invalid input")
    else:
        asset["current_ans"] = np.array(asset["current_ans"])
        transit("elementary2")


def show_elementary():
    global root, scr, urow, ucol, stage, asset
    print("solving elementary")
    total = asset["current_mat"].shape
    all_ent = []
    for i in range(total[0]):
        urow += 1
        ucol = 0
        for j in range(total[1]):
            new_lab = Label(root, text=str(asset["current_mat"][i, j]))
            new_lab.grid(row=urow, column=mc())
            scr.append(new_lab)
        new_ent = Entry(root, width=5)
        new_ent.grid(row=urow, column=mc())
        scr.append(new_ent)
        all_ent.append(new_ent)

    solve_btn = Button(root, text="Solve",
                       command=lambda: validate_elementary(all_ent))
    cancel_btn = Button(root, text="Cancel", command=lambda: transit("main"))
    scr.append(solve_btn)
    scr.append(cancel_btn)
    solve_btn.grid(row=mr(), column=0)
    cancel_btn.grid(row=mr(), column=0)
    # add another input
    # result = elemental(asset["current_mat"])
    # print(result)


def show_matfunc2():
    global root, scr, urow, ucol, stage, asset
    root.title("Matrix Calculator: Functions >> Select Matrix")
    mat_lb = Listbox(root)
    home_btn = Button(root, text="Home", command=lambda: transit("main"))
    mat_lab = Label(root, text="")
    mat_show = Button(root, text="Preview Matrix",
                      command=lambda: disp_matlist(mat_lb, mat_lab, "disp"))
    next_btn = Button(root, text="Next",
                      command=lambda: validate_matfunc(mat_lb))
    for i in range(len(asset["all_mat"])):
        mat_lb.insert(END, asset["all_mat"][i][0])
    scr.append(home_btn)
    scr.append(mat_lb)
    scr.append(mat_lab)
    scr.append(mat_show)
    scr.append(next_btn)
    mat_lb.grid(row=mr(), column=ucol)
    mat_show.grid(row=mr(), column=ucol)
    next_btn.grid(row=mr(), column=ucol)
    home_btn.grid(row=mr(), column=ucol)
    mat_lab.grid(row=mr(), column=ucol)


def next1_matfunc(f):
    global root, scr, urow, ucol, stage, asset
    sf = f.get(ANCHOR)
    asset["current_func"] = ""
    if sf == "":
        messagebox.showerror(title="Matrix Function Error",
                             message="Please select any function first")
        return
    for i in range(len(asset["all_func"])):
        if asset["all_func"][i] == sf:
            asset["current_func"] = sf
    if asset["current_func"] != "":
        transit("matfunc2")


def show_matfunc():
    print("in progress")
    root.title("Matrix Calculator: Functions >> Select Function")
    func_lb = Listbox(root)
    back_btn = Button(root, text="Back", command=lambda: transit("main"))
    next_btn = Button(root, text="Next",
                      command=lambda: next1_matfunc(func_lb))
    for i in range(len(asset["all_func"])):
        func_lb.insert(END, asset["all_func"][i])
    func_lb.grid(row=urow, column=ucol)
    next_btn.grid(row=mr(), column=ucol)
    back_btn.grid(row=mr(), column=ucol)
    scr.append(back_btn)
    scr.append(next_btn)
    scr.append(func_lb)


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
    pastemat_btn = Button(root, text="Paste Matrix",
                          command=lambda: transit("pastemat"))
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
    root.geometry("1000x700")
    hilabel = Label(root, text="Welcome to Matrix Calculator")
    creatorlabel = Label(root, text="Created by Naphat and Samita")
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


def def_mat():
    global root, scr, urow, ucol, stage, asset
    a = np.array(np.mat('1,2,3;4,5,6'))
    b = np.array(np.mat('2,1,1;6,4,5;4,1,3'))
    asset["all_mat"].append(["matrix_A", a])
    asset["all_mat"].append(["matrix_B", b])


def dummy():
    print("hello debug...")
    messagebox.showwarning(title="Matrix Calculator: Debug Warning",
                           message="This function is not available yet")


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
    elif stage == "matfunc2":
        show_matfunc2()
    elif stage == "elementary":
        show_elementary()
    elif stage == "pastemat":
        show_pastemat()
    elif stage == "elementary2":
        show_elementary2()


if __name__ == '__main__':
    root = Tk()
    # root.configure(bg="#DDDDDD")
    scr = []
    allmat = []
    urow = 0
    ucol = 0
    asset = {}
    asset["all_mat"] = []
    asset["all_func"] = ["Elementary", "Inverse"]
    stage = "main"
    summon()
    def_btn()
    def_mat()

    root.mainloop()
