from tkinter import *
from tkinter import messagebox
import numpy as np
import random
import pyperclip as pc
# from textwrap import wrap
from matfunc import *

np.set_printoptions(threshold=np.inf, linewidth=np.inf)


def ansvalid_pastemat(allent):
    global root, scr, urow, ucol, stage, asset
    p = str(pc.paste())
    try:
        newm = np.array(np.mat(p))
        t = newm.shape
        tr = t[0]
        tc = t[1]
        if tc != 1:
            print("err")
            messagebox.showerror(title="Paste Matrix Error",
                                 message="Invalid number of column, please check your clipboard value")
            return
        if tr <= 0 or tr > len(allent):
            print("err")
            messagebox.showerror(title="Paste Matrix Error",
                                 message="Invalid number of row, please check your clipboard value")
            return
        # loop allent to paste each index
        i = 0
        while i < len(allent):
            # e = allent[i].get("1.0", END)
            allent[i].delete(0, END)
            allent[i].insert('end', str(newm[i, 0]))
            i += 1
        return

    except:
        print('ans paste err')
        messagebox.showerror(title="Paste Matrix Error",
                             message="Invalid input, please check your clipboard value")
        return


def save_pastemat(cd, rd, ent, name):
    global root, scr, urow, ucol, stage, asset
    if name.get() == "":
        messagebox.showerror(title="Create Matrix Error",
                             message="Matrix name must not be empty")
        return
    e = ent.get("1.0", END)
    # e = ent.get()
    # print(e)
    err = ""
    try:
        newm = np.array(np.mat(e))
        print(newm)
    except:
        err = "Invalid input, please check your pasted text"

    if err == "":
        sh = newm.shape
        if sh[0] > 15 or sh[1] > 15:
            err = "Invalid Matrix Size (15x15 Limitation Exceeded), Please use Quick function instead"

    if err == "":
        newname = namer_fixedmat(name.get())
        print(newname)
        asset["all_mat"].append([newname, newm])
        messagebox.showinfo(title="Create Matrix Success",
                            message=err)
        transit("main")

    if err != "":
        messagebox.showerror(title="Create Matrix Error",
                             message="Invalid input, please check your pasted text")


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
    paste_ent.grid(row=urow, column=ucol, sticky='news')
    paste_btn.grid(row=mr(), column=ucol, sticky='news')
    name_lab.grid(row=mr(), column=ucol, sticky='news')
    name_ent.grid(row=urow, column=ucol+1, sticky='news')
    save_btn.grid(row=mr(), column=ucol, sticky='news')
    home_btn.grid(row=mr(), column=ucol, sticky='news')
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
    print("test d")
    print(0)
    print(round(0, 2))
    print(len(str(round(0, 2))))
    np.round(m, 2)
    r = rc[0]
    c = rc[1]
    mx = np.max(m)
    mn = np.min(m)
    if len(str(round(mx, 2))) > len(str(round(mn, 2))):
        amx = len(str(round(mx, 2)))
    else:
        amx = len(str(round(mn, 2)))
    # b = m
    # export matrix
    for i in range(r):
        for j in range(c):
            # b += str(m[i, j]) + "  "
            if j == 0:
                b += "| "
            else:
                b += " "
            # if round(m[i, j]) > 0:
            #     b += "  "
            if len(str(round(m[i, j], 2))) == len(str(m[i, j])):
                b += "  "
            b += " "*(amx - len(str(round(m[i, j], 2))))
            b += str(round(m[i, j], 2)) + "  |"
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


def random_ansmat(all_ent):
    global root, scr, urow, ucol, stage, asset
    for c, entry in enumerate(all_ent):
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
    mat_lb.grid(row=urow, column=0, sticky='news')
    mat_show.grid(row=mr(), column=0, sticky='news')
    mat_export.grid(row=mr(), column=0, sticky='news')
    back_btn.grid(row=mr(), column=0, sticky='news')
    mat_lab.grid(row=mr(), column=0, sticky='news')
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
    random_btn.grid(row=asset["fixedmat_r"]+1, column=0, sticky='news')
    name_lab.grid(row=asset["fixedmat_r"]+2, column=0, sticky='news')
    name_ent.grid(row=asset["fixedmat_r"]+2, column=1, sticky='news')
    save_btn.grid(row=asset["fixedmat_r"]+3, column=0, sticky='news')
    canc_btn = Button(root, text='Cancel', command=lambda: transit("main"))
    canc_btn.grid(row=asset["fixedmat_r"]+4, column=0, sticky='news')
    scr.append(canc_btn)
    scr.append(save_btn)
    scr.append(name_lab)
    scr.append(name_ent)
    scr.append(random_btn)


def paste_ansmat(all_ent):
    d = 1
    # try convert mat
    # loop all_ent
    # paste each element in ent


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
            print("Elementary func..")
            transit("elementary")
        if asset["current_func"] == "Inverse":
            print("Inverse func..")
            transit("inverse")
    else:
        messagebox.showerror(title="Matrix Function Error",
                             message="Something went wrong")


def save_setting(o, c, e, t, d, cat, rr):
    global root, scr, urow, ucol, stage, asset
    print("Saving setting...")
    asset["o_set"] = o.get()
    asset["cons_set"] = c.get()
    asset["e_set"] = e.get()
    asset["t_set"] = t.get()
    asset["d_set"] = d.get()
    asset["cat_set"] = cat.get()
    asset["rr_set"] = rr.get()

    print("go home")
    transit("main")


def init_setting(o, c, e, t, d, cat, rr):
    global root, scr, urow, ucol, stage, asset
    o = asset["o_set"]
    c = asset["cons_set"]
    e = asset["e_set"]
    t = asset["t_set"]
    d = asset["d_set"]
    cat = asset["cat_set"]
    rr = asset["rr_set"]


def show_setting():
    global root, scr, urow, ucol, stage, asset

    root.title("Matrix Calculator: Summary Export Setting")

    o_var = IntVar()
    o_box = Checkbutton(root, text="Original Matrix", variable=o_var)
    EL = Label(root, text=">> Elementary Setting")
    con_var = IntVar()
    con_box = Checkbutton(
        root, text="Consistency Validation", variable=con_var)

    e_var = IntVar()
    e_box = Checkbutton(root, text="E Matrix", variable=e_var)

    tri_var = IntVar()
    tri_box = Checkbutton(root, text="Triangular Matrix", variable=tri_var)
    IL = Label(root, text=">> Inverse Setting")
    det_var = IntVar()
    det_box = Checkbutton(root, text="Determinant", variable=det_var)

    concat_var = IntVar()
    concat_box = Checkbutton(
        root, text="Concatenated Matrix", variable=concat_var)

    rref_var = IntVar()
    rref_box = Checkbutton(root, text="Reduced Row Echelon", variable=rref_var)

    o_var.set(asset["o_set"])
    con_var.set(asset["cons_set"])
    e_var.set(asset["e_set"])
    tri_var.set(asset["t_set"])
    det_var.set(asset["d_set"])
    concat_var.set(asset["cat_set"])
    rref_var.set(asset["rr_set"])

    scr.append(o_box)
    scr.append(con_box)
    scr.append(e_box)
    scr.append(tri_box)
    scr.append(det_box)
    scr.append(concat_box)
    scr.append(rref_box)
    scr.append(EL)
    scr.append(IL)
    o_box.grid(row=mr(), column=0, sticky='news')
    EL.grid(row=mr(), column=0, sticky='news')
    con_box.grid(row=mr(), column=0, sticky='news')
    e_box.grid(row=mr(), column=0, sticky='news')
    tri_box.grid(row=mr(), column=0, sticky='news')
    IL.grid(row=mr(), column=0, sticky='news')
    det_box.grid(row=mr(), column=0, sticky='news')
    concat_box.grid(row=mr(), column=0, sticky='news')
    rref_box.grid(row=mr(), column=0, sticky='news')

    save_btn = Button(root, text="Save", command=lambda: save_setting(
        o_var, con_var, e_var, tri_var, det_var, concat_var, rref_var))
    scr.append(save_btn)
    save_btn.grid(row=mr(), column=0, sticky='news')

    home_btn = Button(root, text="Cancel", command=lambda: transit("main"))
    scr.append(home_btn)
    home_btn.grid(row=mr(), column=0, sticky='news')


def show_inverse():
    global root, scr, urow, ucol, stage, asset
    root.title("Matrix Calculator: Functions >> Result (Inverse)")
    newm = np.array(asset["current_mat"])
    tt = newm.shape
    ar = tt[0]
    ac = tt[1]
    result = inverse(asset["current_mat"])
    print(result)
    # checking if its rectangle
    summa = ""

    if result["reason"] == "Since it is rectangle matrix so it is not invertible":
        summa += "Since it is rectangle matrix so it is not invertible"
        if asset["o_set"] == 1:
            summa += "\n Original Matrix: \n"
            summa += beauty_mat(newm)
        r_label = Label(root, text=result["reason"])
        scr.append(r_label)
        r_label.grid(row=mr(), column=ucol)

        pc.copy(summa)
        export_btn = Button(root, text="Export Summary",
                            command=lambda: pc.copy(summa))
        scr.append(export_btn)
        export_btn.grid(row=mr(), column=ucol)
        home_btn = Button(root, text="Home", command=lambda: transit("main"))
        scr.append(home_btn)
        home_btn.grid(row=mr(), column=ucol)

        return

    master_frame = Frame(root, bd=3,
                         relief=RIDGE)
    # master_frame = Frame(root, bg='Light Blue', bd=3,
    #                      relief=RIDGE)
    master_frame.grid(sticky=NSEW)
    master_frame.columnconfigure(0, weight=1)

    frame1 = Frame(master_frame, bg='Green', bd=2, relief=FLAT)
    frame1.grid(row=1, column=0, sticky=NW)

    frame2 = Frame(master_frame, bd=2, relief=FLAT)
    frame2.grid(row=3, column=0, sticky=NW)

    # Add a canvas in that frame.
    canvas = Canvas(frame2, bg='Yellow')
    canvas.grid(row=0, column=0)

    # Create a vertical scrollbar linked to the canvas.
    vsbar = Scrollbar(frame2, orient=VERTICAL, command=canvas.yview)
    vsbar.grid(row=0, column=1, sticky=NS)
    canvas.configure(yscrollcommand=vsbar.set)

    # Create a horizontal scrollbar linked to the canvas.
    hsbar = Scrollbar(frame2, orient=HORIZONTAL, command=canvas.xview)
    hsbar.grid(row=1, column=0, sticky=EW)
    canvas.configure(xscrollcommand=hsbar.set)

    # Create a frame on the canvas to contain the grid of buttons.
    buttons_frame = Frame(canvas)

    ROWS, COLS = 200, 10  # Size of grid.
    ROWS_DISP = 3  # Number of rows to display.
    COLS_DISP = 2  # Number of columns to display.
    test_row = 10

    print("checking row col")
    if ar >= ac:
        test_row = ar**2
    else:
        test_row = ar**2
    ROWS = test_row
    print("done checking")
    # check det
    sumdet = "\nDeterminant Triangular Form: \n"
    det_lab = Label(buttons_frame, text="Finding Determinant: ")
    det_lab.grid(row=urow, column=ucol)
    scr.append(det_lab)
    # disp detlog
    urow += 1
    limitcol = 4
    for i in range(len(result["detlog"])):
        if ucol >= limitcol:
            urow += 1
            ucol = 0
        detlog = beauty_mat(result["detlog"][i])
        det_log = Label(buttons_frame, text=detlog)
        scr.append(det_log)
        det_log.grid(row=urow, column=mc())
    if len(result["detlog"]) > 0:
        sumdet += beauty_mat(result["detlog"][-1])
    # disp det result
    urow += 1
    ucol = 0
    sumdet += "\nDeterminant Result: \n"
    det_result = Label(buttons_frame, text="Determinant Result: ")
    det_result.grid(row=urow, column=ucol)
    scr.append(det_result)
    sumdet += result["detresult"]
    det_result2 = Label(buttons_frame, text=result["detresult"])
    det_result2.grid(row=urow, column=mc())
    scr.append(det_result2)
    if not result["invertible"]:
        ucol = 0
        summa += result["reason"]
        r_label = Label(buttons_frame, text=result["reason"])
        scr.append(r_label)
        r_label.grid(row=mr(), column=ucol)
        if asset["o_set"] == 1:
            summa += "\n Original Matrix: \n"
            summa += beauty_mat(newm)
        if asset["d_set"] == 1:
            summa += sumdet
        pc.copy(summa)
        export_btn = Button(root, text="Export Summary",
                            command=lambda: pc.copy(summa))
        scr.append(export_btn)
        export_btn.grid(row=mr(), column=ucol)
        home_btn = Button(root, text="Home", command=lambda: transit("main"))
        scr.append(home_btn)
        home_btn.grid(row=mr(), column=ucol)

        canvas.create_window((0, 0), window=buttons_frame, anchor=NW)

        buttons_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(ALL)  # Get bounding box of canvas with Buttons.
        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
        canvas.configure(scrollregion=bbox, width=dw, height=dh)
        scr.append(canvas)
        scr.append(buttons_frame)
        scr.append(hsbar)
        scr.append(vsbar)
        scr.append(master_frame)
        scr.append(frame1)
        scr.append(frame2)
        return

    # disp +E
    urow += 1
    ucol = 0
    sume = "\nConcatenate with Identity matrix: \n"
    E_result = Label(buttons_frame, text="Concatenate with Identity matrix: ")
    E_result.grid(row=urow, column=ucol)
    scr.append(E_result)
    sume += beauty_mat(result["invlog"][0])
    E_result2 = Label(buttons_frame, text=beauty_mat(result["invlog"][0]))
    E_result2.grid(row=urow, column=mc())
    scr.append(E_result2)
    # disp rref
    urow += 1
    ucol = 0
    sumrref = "\nReduced Row Echelon Form:\n"
    RE_result = Label(buttons_frame, text="Doing Reduced Row Echelon Form: ")
    RE_result.grid(row=urow, column=ucol)
    scr.append(RE_result)
    for i in range(len(result["rreflog"])):
        if ucol >= limitcol:
            urow += 1
            ucol = 0
        rrlog = beauty_mat(result["rreflog"][i])
        rr_log = Label(buttons_frame, text=rrlog)
        scr.append(rr_log)
        rr_log.grid(row=urow, column=mc())
    # disp final inv
    if len(result["rreflog"]) > 0:
        sumrref += beauty_mat(result["rreflog"][-1])
    urow += 1
    ucol = 0
    summa += "\n Inversed Matrix: \n"
    IE_result = Label(buttons_frame, text="Inversed Matrix: ")
    IE_result.grid(row=urow, column=ucol)
    scr.append(IE_result)
    IE_result2 = Label(buttons_frame, text=beauty_mat(result["inverted"]))
    summa += beauty_mat(result["inverted"])
    IE_result2.grid(row=urow, column=mc())
    scr.append(IE_result2)
    ucol = 0

    if asset["o_set"] == 1:
        summa += "\n Original Matrix: \n"
        summa += beauty_mat(newm)
    if asset["d_set"] == 1:
        summa += sumdet
    if asset["cat_set"] == 1:
        summa += sume
    if asset["rr_set"] == 1:
        summa += sumrref
    pc.copy(summa)
    export_btn = Button(root, text="Export Summary",
                        command=lambda: pc.copy(summa))
    scr.append(export_btn)
    export_btn.grid(row=mr(), column=ucol)
    home_btn = Button(root, text="Home", command=lambda: transit("main"))
    scr.append(home_btn)
    home_btn.grid(row=mr(), column=ucol)

    canvas.create_window((0, 0), window=buttons_frame, anchor=NW)
    buttons_frame.update_idletasks()  # Needed to make bbox info available.
    bbox = canvas.bbox(ALL)  # Get bounding box of canvas with Buttons.
    w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
    dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
    canvas.configure(scrollregion=bbox, width=dw, height=dh)
    scr.append(canvas)
    scr.append(buttons_frame)
    scr.append(hsbar)
    scr.append(vsbar)
    scr.append(master_frame)
    scr.append(frame1)
    scr.append(frame2)


def show_quickelem2():
    global root, scr, urow, ucol, stage, asset
    root.title("Matrix Calculator: Functions >> Result (Quick Elementary)")
    asset["quick_mat"] = np.round(asset["quick_mat"], 30)
    asset["quick_ansmat"] = np.round(asset["quick_ansmat"], 30)
    firstleft = np.array(asset["quick_mat"])
    firstright = np.array(asset["quick_ansmat"])
    result = elemental(asset["quick_mat"], asset["quick_ansmat"])
    # export summary_btn
    res_text = "\n Quick Elementary Result Summary\n"

    res_text += "\n"+str(result["consistresult"][0])+"\n"
    if result["consist"]:
        if len(result["freevar"]) > 0:
            # looping var for free var
            summa_free = "\n All Variables Value\n"
            newresult = ""
            cot = 0
            summer = 0
            for rt in range(len(result["result_text"])):
                # print(newresult)
                if cot >= 20:
                    newresult += "\n"
                    cot = 0
                if summer >= 100:
                    summer = 0
                    summa_free += "\n"
                summa_free += result["result_text"][rt]
                newresult += result["result_text"][rt]
                cot += 1
            res_text += summa_free

            res_text += "\n Original Matrix\n"
            res_text += str(firstleft)
            res_text += "\n Answer(B) Matrix\n"
            res_text += str(firstright)
        else:
            iv = len(result["var"])-1
            iiv = 1
            vt = ""
            while iv >= 0:
                vt += "x"+str(iiv)+" = "+str(round(result["var"][iv], 2))

                if iv != 0:
                    vt += ", "
                if len(vt) % 50 >= 1:
                    vt += "\n"
                iv -= 1
                iiv += 1
            res_text += vt
            res_text += "\n Original Matrix\n"
            res_text += str(firstleft)
            res_text += "\n Answer(B) Matrix\n"
            res_text += str(firstright)
    else:
        res_text += "\n Original Matrix\n"
        res_text += str(firstleft)
        res_text += "\n Answer(B) Matrix\n"
        res_text += str(firstright)
    pc.copy(res_text)
    export_btn = Button(root, text="Export Summary",
                        command=lambda: pc.copy(res_text))
    scr.append(export_btn)
    export_btn.grid(row=mr(), column=ucol)
    # home_btn
    home_btn = Button(root, text="Home",
                      command=lambda: transit("main"))
    scr.append(home_btn)
    home_btn.grid(row=mr(), column=ucol)


def randsolve_pastequick(re, ce):
    global root, scr, urow, ucol, stage, asset
    print("random and solve quick")
    err = ""
    if re.get().isdigit() and ce.get().isdigit():
        r = int(re.get())
        c = int(ce.get())
        if r <= 0 or c <= 0:
            err = "Input cannot be lower than 1"

    else:
        err = "Input has to be an integer"
    if err == "":
        print("rand after r c")
        newm = np.random.rand(r, c)
        newa = np.random.rand(r, 1)
        # random after r c
        print("solving randquick")
        asset["quick_mat"] = newm
        asset["quick_ansmat"] = newa
        print("newm")
        print(newm)
        print(newm)
        print(asset["quick_mat"])
        transit("quickelem_result")
    else:
        re.delete(0, END)
        ce.delete(0, END)
        print("show msg box err")
        messagebox.showerror(title="Solve Random Matrix Error", message=err)


def solve_pastequick(ent):
    global root, scr, urow, ucol, stage, asset
    print("solve paste quick")
    err = ""
    coef = ent.get("1.0", END)
    try:
        newm = np.array(np.mat(coef))
    except:
        err = "Coefficient Text Invalid, Please check your input"
    ans = str(pc.paste())

    try:
        newa = np.array(np.mat(ans))
    except:

        err = "Answer(B) Text Invalid, Please check your clipboard value"
    if err == "":
        print("we can go")
        snewa = newa.shape
        snewm = newm.shape
        if snewa[0] != snewm[0]:
            err = "Number of Coefficient and Answer(B) Matrix Rows mismatched, Please check your input"
        if snewa[1] != 1:
            err = "Number of Answer(B) Matrix Column invalid"
    if err != "":
        messagebox.showerror(title="Solve Pasted Matrix Error",
                             message=err)
    else:
        print("solving pastequick")
        asset["quick_mat"] = newm
        asset["quick_ansmat"] = newa
        transit("quickelem_result")


def solve_augmented():
    err = ""
    try:
        augm = np.array(np.mat(pc.paste()))
    except:
        err = "Invalid Augmented Matrix, Please check your clipboard value"
    if err == "":
        sh = augm.shape
        if sh[1] <= 1 or sh[0] <= 0:
            err = "Augmented Matrix insufficient column, It should be more than 1 column"

        else:
            newm = augm[:, :-1]
            newa = augm[:, -1].reshape(-1, 1)
    if err != "":
        messagebox.showerror(title="Solve Pasted AugmentedMatrix Error",
                             message=err)
    else:
        print("solving pastequick")
        asset["quick_mat"] = newm
        asset["quick_ansmat"] = newa
        transit("quickelem_result")


def pastesolve_quickinv():
    global root, scr, urow, ucol, stage, asset
    err = ""
    try:
        newm = np.array(np.mat(pc.paste()))
        s = newm.shape
        if s[0] <= 0:
            err = "Input Matrix Size,At least one column required"
    except:
        err = "Input Invalid, Please check your clipboard value"

    if err != "":
        messagebox.showerror(title="Solve Pasted AugmentedMatrix Error",
                             message=err)
    else:
        asset["quick_mat"] = newm
        transit("quickinv_result")


def randsolve_quickinv(ent):
    global root, scr, urow, ucol, stage, asset
    err = ""
    if ent.get().isdigit():
        r = int(ent.get())
        if r <= 0:
            err = "Input cannot be lower than 1"

    else:
        err = "Input has to be an integer"
    if err == "":
        print("rand after r c")
        newm = np.random.rand(r, r)
        asset["quick_mat"] = newm
        transit("quickinv_result")
    else:
        ent.delete(0, END)
        print("show msg box err")
        messagebox.showerror(title="Solve Random Matrix Error", message=err)


def show_quickinv2():
    global root, scr, urow, ucol, stage, asset
    root.title("Matrix Calculator: Functions >> Result (Quick Inverse)")
    newm = np.array(asset["quick_mat"])
    tt = newm.shape
    ar = tt[0]
    ac = tt[1]
    result = inverse(asset["quick_mat"])
    res_text = ""
    res_text += "\n Quick Inverse Result\n"
    res_text += "\n Determinant\n"
    if len(result["detlog"]) > 0:
        # res_text += beauty_mat(result["detlog"][-1])
        res_text += result["detresult"] + "\n"

    if not result["invertible"]:
        res_text += result["reason"] + "\n"
    res_text += "\n Inversed Matrix\n"
    res_text += beauty_mat(result["inverted"])
    res_text += "\n Original Matrix\n"
    res_text += beauty_mat(newm)

    pc.copy(res_text)
    export_btn = Button(root, text="Export Summary",
                        command=lambda: pc.copy(res_text))
    scr.append(export_btn)
    export_btn.grid(row=mr(), column=ucol)
    # home_btn
    home_btn = Button(root, text="Home",
                      command=lambda: transit("main"))
    scr.append(home_btn)
    home_btn.grid(row=mr(), column=ucol)


def show_quickinv():
    global root, scr, urow, ucol, stage, asset
    root.title("Matrix Calculator: Functions >> Quick Inverse")
    paste_lab = Label(root, text="Paste Matrix")
    paste_btn = Button(root, text="Paste and Solve",
                       command=lambda: pastesolve_quickinv())
    random_lab = Label(root, text="Random Matrix")
    cr_lab = Label(root, text="Number of Column & Row: ")
    cr_ent = Entry(root, width=5)
    randsolev_btn = Button(root, text="Random and Solve",
                           command=lambda: randsolve_quickinv(cr_ent))

    scr.append(paste_lab)
    scr.append(paste_btn)
    scr.append(random_lab)
    scr.append(cr_lab)
    scr.append(cr_ent)
    scr.append(randsolev_btn)

    paste_lab.grid(row=mr(), column=ucol)
    paste_btn.grid(row=mr(), column=ucol)
    random_lab.grid(row=mr(), column=ucol)
    cr_lab.grid(row=mr(), column=ucol)
    cr_ent.grid(row=urow, column=ucol+1)
    randsolev_btn.grid(row=mr(), column=ucol)

    home_btn = Button(root, text="Home",
                      command=lambda: transit("main"))
    scr.append(home_btn)
    home_btn.grid(row=mr(), column=ucol)


def show_quickelem():
    global root, scr, urow, ucol, stage, asset
    root.title("Matrix Calculator: Functions >> Quick Elementary")
    # paste --> m_ent,a_ent,pastem_btn,pastea_btn,solve_pasted_btn
    paste_lab = Label(root, text="Paste Matrix")
    augpaste_btn = Button(root, text="Paste as Augmented Matrix and Solve",
                          command=lambda: solve_augmented())
    mpaste_ent = Text(root, width=30, height=10, bg="#EEEEEE")
    # apaste_ent = Text(root, width=30, height=10, bg="#EEEEEE")
    mpaste_btn = Button(root, text="Paste Coefficient Matrix",
                        command=lambda: paste_pastemat(mpaste_ent))

    apaste_btn = Button(root, text="Paste B Matrix And Solve",
                        command=lambda: solve_pastequick(mpaste_ent))
    scr.append(paste_lab)
    scr.append(augpaste_btn)
    scr.append(mpaste_ent)
    # scr.append(apaste_ent)
    scr.append(mpaste_btn)
    scr.append(apaste_btn)

    paste_lab.grid(row=mr(), column=ucol)
    augpaste_btn.grid(row=mr(), column=ucol)
    mpaste_ent.grid(row=mr(), column=ucol)
    mpaste_btn.grid(row=mr(), column=ucol)
    apaste_btn.grid(row=mr(), column=ucol)
    # random --> row_ent,col_ent,solve_random_btn
    random_lab = Label(root, text="Random Matrix")
    row_lab = Label(root, text="Number of Row: ")
    col_lab = Label(root, text="Number of Column: ")
    row_ent = Entry(root, width=5)
    col_ent = Entry(root, width=5)
    randsolev_btn = Button(root, text="Random and Solve",
                           command=lambda: randsolve_pastequick(row_ent, col_ent))

    scr.append(random_lab)
    scr.append(row_lab)
    scr.append(col_lab)
    scr.append(row_ent)
    scr.append(col_ent)
    scr.append(randsolev_btn)

    random_lab.grid(row=mr(), column=ucol)
    row_lab.grid(row=mr(), column=ucol)
    row_ent.grid(row=urow, column=ucol+1)
    col_lab.grid(row=mr(), column=ucol)
    col_ent.grid(row=urow, column=ucol+1)
    randsolev_btn.grid(row=mr(), column=ucol)
    # home_btn

    home_btn = Button(root, text="Home",
                      command=lambda: transit("main"))
    scr.append(home_btn)
    home_btn.grid(row=mr(), column=ucol)


def show_elementary2():
    global root, scr, urow, ucol, stage, asset
    root.title("Matrix Calculator: Functions >> Result (Elementary)")
    firstleft = np.array(asset["current_mat"])
    firstright = np.array(asset["current_ans"])
    result = elemental(asset["current_mat"], asset["current_ans"])
    summa = ""
    summa_ori = "\nOriginal Coefficient Matrix\n"
    summa_ori += beauty_mat(firstleft)
    summa_ori += "\nOriginal B Matrix\n"
    summa_ori += beauty_mat(firstright)

    # testing area open

    # test 2
    master_frame = Frame(root, bd=3,
                         relief=RIDGE)
    # master_frame = Frame(root, bg='Light Blue', bd=3,
    #                      relief=RIDGE)
    master_frame.grid(sticky=NSEW)
    master_frame.columnconfigure(0, weight=1)

    # label1 = Label(
    #     master_frame, text='Frame1 Contendasdsadddsadasdasdasdasdasadsadsadasdasdadats')
    # label1.grid(row=0, column=0, pady=5, sticky=NW)

    frame1 = Frame(master_frame, bg='Green', bd=2, relief=FLAT)
    frame1.grid(row=1, column=0, sticky=NW)

    # cb_var1 = IntVar()
    # checkbutton1 = Checkbutton(frame1, text='StartCheckBox', variable=cb_var1)
    # checkbutton1.grid(row=0, column=0, padx=0, pady=0)

    # label2 = Label(master_frame, text='Frame2 Contents')
    # label2.grid(row=2, column=0, pady=5, sticky=NW)

    # Create a frame for the canvas and scrollbar(s).
    # frame2 = Frame(master_frame, bg='Red', bd=2, relief=FLAT)
    # frame2.grid(row=3, column=0, sticky=NW)
    frame2 = Frame(master_frame, bd=2, relief=FLAT)
    frame2.grid(row=3, column=0, sticky=NW)

    # Add a canvas in that frame.
    canvas = Canvas(frame2, bg='Yellow')
    canvas.grid(row=0, column=0)

    # Create a vertical scrollbar linked to the canvas.
    vsbar = Scrollbar(frame2, orient=VERTICAL, command=canvas.yview)
    vsbar.grid(row=0, column=1, sticky=NS)
    canvas.configure(yscrollcommand=vsbar.set)

    # Create a horizontal scrollbar linked to the canvas.
    hsbar = Scrollbar(frame2, orient=HORIZONTAL, command=canvas.xview)
    hsbar.grid(row=1, column=0, sticky=EW)
    canvas.configure(xscrollcommand=hsbar.set)

    # Create a frame on the canvas to contain the grid of buttons.
    buttons_frame = Frame(canvas)

    ROWS, COLS = 200, 10  # Size of grid.
    ROWS_DISP = 3  # Number of rows to display.
    COLS_DISP = 2  # Number of columns to display.
    test_row = 10
    print("checking row col")
    if result["allr"] >= result["allc"]:
        test_row = result["allr"]**2
    else:
        test_row = result["allr"]**2
    ROWS = test_row
    print("done checking")
    # ROWS, COLS = 10, 6  # Size of grid.
    # ROWS_DISP = 3  # Number of rows to display.
    # COLS_DISP = 4  # Number of columns to display.
    # , width=1000
    # showing area open
    # hilabel = Label(
    #     buttons_frame, text="Welcome to Matrix Calculator")
    # creatorlabel = Label(
    #     buttons_frame, text="Created by Naphat and Samita")
    # matter_btn = Button(buttons_frame, text="Create Matrix",
    #                     command=lambda: transit("createmat"))
    # matlist_btn = Button(buttons_frame, text="Matrix List",
    #                      command=lambda: transit("matlist"))
    # matfunc_btn = Button(buttons_frame, text="Do Functions",
    #                      command=lambda: transit("matfunc"))
    # exit_btn = Button(buttons_frame, text="Quit",
    #                   command=exitProg)

    # hilabel.grid(row=urow, column=ucol)
    # creatorlabel.grid(row=mr(), column=ucol, sticky='news')
    # matter_btn.grid(row=mr(), column=ucol, sticky='news')
    # matlist_btn.grid(row=mr(), column=ucol, sticky='news')
    # matfunc_btn.grid(row=mr(), column=ucol, sticky='news')
    # exit_btn.grid(row=mr(), column=ucol, sticky='news')
    consist_lab = Label(buttons_frame, text="Checking consistency: ")
    consist_lab.grid(row=urow, column=ucol)
    scr.append(consist_lab)
    summa_cons = "Consistency Validation\n"
    # looping consist disp
    conlog = result["consistlog"]
    for i in range(len(conlog)):
        ct = beauty_mat(conlog[i])
        if i == len(conlog)-2:
            summa_cons += ct
        cl = Label(buttons_frame, text=ct)
        scr.append(cl)
        if ucol >= 4:
            urow += 1
            ucol = 0
        cl.grid(row=urow, column=mc())

    conresult = Label(buttons_frame, text=result["consistresult"][0])
    summa_cons += "\n"+str(result["consistresult"][0])
    scr.append(conresult)
    ucol = 0
    conresult.grid(row=mr(), column=ucol)

    if not result["consist"]:

        if asset["o_set"] == 1:
            summa += summa_ori
        if asset["cons_set"] == 1:
            summa += summa_cons
        export_btn = Button(root, text="Export Summary",
                            command=lambda: pc.copy(summa))
        scr.append(export_btn)
        home_btn = Button(root, text="Home",
                          command=lambda: transit("main"))
        scr.append(home_btn)
        home_btn.grid(row=mr(), column=ucol)

        canvas.create_window((0, 0), window=buttons_frame, anchor=NW)

        buttons_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(ALL)  # Get bounding box of canvas with Buttons.

        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        ROWS = 5
        # COLS = 10
        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
        canvas.configure(scrollregion=bbox, width=dw, height=dh)
        pc.copy(summa)
        scr.append(canvas)
        scr.append(buttons_frame)
        scr.append(hsbar)
        scr.append(vsbar)
        scr.append(master_frame)
        scr.append(frame1)
        scr.append(frame2)
        return
    if len(result["freevar"]) > 0:
        # looping var for free var
        summa_free = "\n All Variables Value\n"
        result_label = Label(buttons_frame, text="All Variables value: ")
        scr.append(result_label)
        result_label.grid(row=mr(), column=ucol)
        newresult = ""
        cot = 0
        summer = 0
        for rt in range(len(result["result_text"])):
            # print(newresult)
            if cot >= 20:
                newresult += "\n"
                cot = 0
            if summer >= 100:
                summer = 0
                summa_free += "\n"
            summa_free += result["result_text"][rt]
            newresult += result["result_text"][rt]
            cot += 1

        result_text = Label(buttons_frame, text=newresult)
        scr.append(result_text)
        summa += summa_free
        if asset["o_set"] == 1:
            summa += summa_ori
        if asset["cons_set"] == 1:
            summa += summa_cons
        summa += "\n"+beauty_mat(result["freevar_ans"])+"\n"
        result_text.grid(row=urow, column=mc())
        home_btn = Button(root, text="Home",
                          command=lambda: transit("main"))
        export_btn = Button(root, text="Export Summary",
                            command=lambda: pc.copy(summa))
        scr.append(export_btn)
        export_btn.grid(row=mr(), column=ucol)
        scr.append(home_btn)
        ucol = 0
        home_btn.grid(row=mr(), column=ucol)

        canvas.create_window((0, 0), window=buttons_frame, anchor=NW)

        buttons_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(ALL)  # Get bounding box of canvas with Buttons.

        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        if len(newresult) > 1000:
            ROWS = int(len(newresult)/100)
        elif len(newresult) > 300:
            ROWS = int(len(newresult)/20)
        else:
            ROWS = 5

        print("make row: ")
        print(ROWS)
        # COLS = 10
        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
        canvas.configure(scrollregion=bbox, width=dw, height=dh)

        scr.append(canvas)
        scr.append(buttons_frame)
        scr.append(hsbar)
        scr.append(vsbar)
        scr.append(master_frame)
        scr.append(frame1)
        scr.append(frame2)
        pc.copy(summa)
        return
    print("generating step and result")
    r = result["entire"]
    print("all r")
    print(r)
    onlye = []
    onlym = []
    onlyr = []
    j = 0
    elim_lab = Label(buttons_frame, text="Eliminating using elementary: ")
    elim_lab.grid(row=mr(), column=ucol)
    scr.append(elim_lab)
    urow += 1
    summa_tri = "\nTriangular Coefficient Matrix\n"
    for i in range(len(r)):
        nl = beauty_mat(r[i])
        nt = Label(buttons_frame, text=nl)
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
        x_lab = Label(buttons_frame, text="x")
        x_lab.grid(row=urow, column=mc())
        scr.append(x_lab)
        onlym[m].grid(row=urow, column=mc())
        next_lab = Label(buttons_frame, text=">>")
        next_lab.grid(row=urow, column=mc())
        scr.append(next_lab)
        onlyr[m].grid(row=urow, column=mc())
        ucol = 0
    if len(onlye) > 0:
        summa_tri += beauty_mat(r[-1])
    else:
        summa_tri += "Original Matrix is already Triangular Matrix"
    summa_e = "\nE Matrix\n"
    ns_lab = Label(buttons_frame, text="Making E matrix:")
    scr.append(ns_lab)
    ns_lab.grid(row=mr(), column=ucol)
    re = result["entire2"]
    jj = 0
    for k in range(len(re)):
        nl2 = beauty_mat(re[k])
        s2 = Label(buttons_frame, text=nl2)
        scr.append(s2)
        if jj == 0:
            s2.grid(row=urow, column=mc())
            jj += 1
        elif jj == 1:
            x_lab = Label(buttons_frame, text="x")
            next_lab = Label(buttons_frame, text=">>")
            scr.append(x_lab)
            scr.append(next_lab)
            if ucol > 7:
                urow += 1
                ucol = 0
            x_lab.grid(row=urow, column=mc())
            s2.grid(row=urow, column=mc())
            next_lab.grid(row=urow, column=mc())
            jj = 0
    if len(re) > 0:
        summa_e += beauty_mat(re[-1])
    else:
        summa_e += "Original Matrix is already Triangular Matrix so no use of E Matrix"
    print(result["firstans"])
    b_ans = beauty_mat(result["firstans"])
    b_lab = Label(buttons_frame, text=b_ans)
    scr.append(b_lab)
    summa_newans = "\nNew B Matrix\n"
    if result["togetans"] != []:
        ucol = 0
        x_lab = Label(buttons_frame, text="x")
        next_lab = Label(buttons_frame, text=">>")
        scr.append(x_lab)
        scr.append(next_lab)
        ns_lab2 = Label(buttons_frame, text="Making new answer matrix:")
        scr.append(ns_lab2)
        ns_lab2.grid(row=mr(), column=ucol)
        r3 = beauty_mat(result["newans"])
        summa_newans += beauty_mat(result["newans"])
        r3_lab = Label(buttons_frame, text=r3)
        scr.append(r3_lab)
        nl2 = beauty_mat(re[-1])
        s2 = Label(buttons_frame, text=nl2)
        scr.append(s2)
        s2.grid(row=urow, column=mc())
        x_lab.grid(row=urow, column=mc())
        b_lab.grid(row=urow, column=mc())
        next_lab.grid(row=urow, column=mc())
        r3_lab.grid(row=urow, column=mc())

    ivar_lab = Label(buttons_frame, text="All variables value: ")
    summa_var = "\nAll Variables Value\n"
    print("all var printing out loud")
    print(result["var"])
    scr.append(ivar_lab)
    ucol = 0
    ivar_lab.grid(row=mr(), column=ucol)
    iv = len(result["var"])-1
    iiv = 1
    vt = ""
    while iv >= 0:
        vt += "x"+str(iiv)+" = "+str(round(result["var"][iv], 2))

        if iv != 0:
            vt += ", "
        if len(vt) % 50 >= 1:
            vt += "\n"
        iv -= 1
        iiv += 1
    summa_var += vt
    var_lab = Label(buttons_frame, text=vt)
    scr.append(var_lab)
    var_lab.grid(row=urow, column=mc())

    ucol = 0
    summa += summa_var
    if asset["o_set"] == 1:
        summa += summa_ori
    if asset["cons_set"] == 1:
        summa += summa_cons
    if asset["t_set"] == 1:
        summa += summa_tri
    if asset["e_set"] == 1:
        summa += summa_e
    if asset["t_set"] == 1:
        summa += summa_newans

    export_btn = Button(root, text="Export Summary",
                        command=lambda: pc.copy(summa))
    scr.append(export_btn)
    export_btn.grid(row=mr(), column=ucol)
    pc.copy(summa)
    home_btn = Button(root, text="Home",
                      command=lambda: transit("main"))
    scr.append(home_btn)
    home_btn.grid(row=mr(), column=ucol)

    # showing area end

    # Add the buttons to the frame.
    # for i in range(1, ROWS+1):
    #     for j in range(1, COLS+1):
    #         button = Label(buttons_frame, padx=7, pady=7,
    #                        activebackground='orange', text='')
    #         button.grid(row=i, column=j, sticky='news')
    # button = Button(buttons_frame, padx=7, pady=7, relief=RIDGE,
    #                 activebackground='orange', text='[%d, %d]' % (i, j))
    # button.grid(row=i, column=j, sticky='news')

    # Create canvas window to hold the buttons_frame.
    canvas.create_window((0, 0), window=buttons_frame, anchor=NW)

    buttons_frame.update_idletasks()  # Needed to make bbox info available.
    bbox = canvas.bbox(ALL)  # Get bounding box of canvas with Buttons.

    # Define the scrollable region as entire canvas with only the desired
    # number of rows and columns displayed.
    w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
    dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
    canvas.configure(scrollregion=bbox, width=dw, height=dh)

    scr.append(canvas)
    scr.append(buttons_frame)
    scr.append(hsbar)
    scr.append(vsbar)
    scr.append(master_frame)
    scr.append(frame1)
    scr.append(frame2)
    print("done elementary")

    # testing area end

    # # disp consist check
    # consist_lab = Label(root, text="Checking consistency: ")
    # consist_lab.grid(row=urow, column=ucol)
    # scr.append(consist_lab)
    # # looping consist disp
    # conlog = result["consistlog"]
    # for i in range(len(conlog)):
    #     ct = beauty_mat(conlog[i])
    #     cl = Label(root, text=ct)
    #     scr.append(cl)
    #     cl.grid(row=urow, column=mc())
    # conresult = Label(root, text=result["consistresult"][0])
    # scr.append(conresult)
    # ucol = 0
    # conresult.grid(row=mr(), column=ucol)

    # if not result["consist"]:
    #     home_btn = Button(root, text="Home", command=lambda: transit("main"))
    #     scr.append(home_btn)
    #     home_btn.grid(row=mr(), column=ucol)
    #     return
    # if len(result["freevar"]) > 0:
    #     # looping var for free var

    #     result_label = Label(root, text="All Variables value: ")
    #     scr.append(result_label)
    #     result_label.grid(row=mr(), column=ucol)
    #     result_text = Label(root, text=result["result_text"])
    #     scr.append(result_text)
    #     result_text.grid(row=urow, column=mc())
    #     home_btn = Button(root, text="Home", command=lambda: transit("main"))
    #     scr.append(home_btn)
    #     ucol = 0
    #     home_btn.grid(row=mr(), column=ucol)
    #     return
    # print("generating step and result")
    # r = result["entire"]
    # print("all r")
    # print(r)
    # onlye = []
    # onlym = []
    # onlyr = []
    # j = 0
    # elim_lab = Label(root, text="Eliminating using elementary: ")
    # elim_lab.grid(row=mr(), column=ucol)
    # scr.append(elim_lab)
    # urow += 1
    # for i in range(len(r)):
    #     nl = beauty_mat(r[i])
    #     nt = Label(root, text=nl)
    #     scr.append(nt)
    #     if j == 0:
    #         onlym.append(nt)
    #         j += 1
    #     elif j == 1:
    #         onlye.append(nt)
    #         j += 1
    #     else:
    #         onlyr.append(nt)
    #         j = 0
    # for m in range(len(onlye)):
    #     onlye[m].grid(row=mr(), column=ucol)
    #     x_lab = Label(root, text="x")
    #     x_lab.grid(row=urow, column=mc())
    #     scr.append(x_lab)
    #     onlym[m].grid(row=urow, column=mc())
    #     next_lab = Label(root, text=">>")
    #     next_lab.grid(row=urow, column=mc())
    #     scr.append(next_lab)
    #     onlyr[m].grid(row=urow, column=mc())
    #     ucol = 0
    # ns_lab = Label(root, text="Making E matrix:")
    # scr.append(ns_lab)
    # ns_lab.grid(row=mr(), column=ucol)
    # re = result["entire2"]
    # jj = 0
    # for k in range(len(re)):
    #     nl2 = beauty_mat(re[k])
    #     s2 = Label(root, text=nl2)
    #     scr.append(s2)
    #     if jj == 0:
    #         s2.grid(row=urow, column=mc())
    #         jj += 1
    #     elif jj == 1:
    #         x_lab = Label(root, text="x")
    #         next_lab = Label(root, text=">>")
    #         scr.append(x_lab)
    #         scr.append(next_lab)
    #         x_lab.grid(row=urow, column=mc())
    #         s2.grid(row=urow, column=mc())
    #         next_lab.grid(row=urow, column=mc())
    #         jj = 0
    # print(result["firstans"])
    # b_ans = beauty_mat(result["firstans"])
    # b_lab = Label(root, text=b_ans)
    # scr.append(b_lab)
    # if result["togetans"] != []:
    #     ucol = 0
    #     x_lab = Label(root, text="x")
    #     next_lab = Label(root, text=">>")
    #     scr.append(x_lab)
    #     scr.append(next_lab)
    #     ns_lab2 = Label(root, text="Making new answer matrix:")
    #     scr.append(ns_lab2)
    #     ns_lab2.grid(row=mr(), column=ucol)
    #     r3 = beauty_mat(result["newans"])
    #     r3_lab = Label(root, text=r3)
    #     scr.append(r3_lab)
    #     nl2 = beauty_mat(re[-1])
    #     s2 = Label(root, text=nl2)
    #     scr.append(s2)
    #     s2.grid(row=urow, column=mc())
    #     x_lab.grid(row=urow, column=mc())
    #     b_lab.grid(row=urow, column=mc())
    #     next_lab.grid(row=urow, column=mc())
    #     r3_lab.grid(row=urow, column=mc())

    # ivar_lab = Label(root, text="All variables value: ")
    # print("all var printing out loud")
    # print(result["var"])
    # scr.append(ivar_lab)
    # ucol = 0
    # ivar_lab.grid(row=mr(), column=ucol)
    # iv = len(result["var"])-1
    # iiv = 1
    # vt = ""
    # while iv >= 0:
    #     vt += "x"+str(iiv)+" = "+str(result["var"][iv])
    #     if iv != 0:
    #         vt += ", "
    #     if len(vt) > 30:
    #         vt += "\n"
    #     iv -= 1
    #     iiv += 1
    # var_lab = Label(root, text=vt)
    # scr.append(var_lab)
    # var_lab.grid(row=urow, column=mc())

    # ucol = 0
    # home_btn = Button(root, text="Home", command=lambda: transit("main"))
    # scr.append(home_btn)
    # home_btn.grid(row=mr(), column=ucol)


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

    random_btn = Button(root, text="Random Answer",
                        command=lambda: random_ansmat(all_ent))
    pastemat_btn = Button(root, text="Paste Answer",
                          command=lambda: ansvalid_pastemat(all_ent))
    solve_btn = Button(root, text="Solve",
                       command=lambda: validate_elementary(all_ent))
    cancel_btn = Button(root, text="Cancel", command=lambda: transit("main"))
    scr.append(solve_btn)
    scr.append(cancel_btn)
    scr.append(random_btn)
    scr.append(pastemat_btn)
    random_btn.grid(row=mr(), column=0, sticky='news')
    pastemat_btn.grid(row=mr(), column=0, sticky='news')
    solve_btn.grid(row=mr(), column=0, sticky='news')
    cancel_btn.grid(row=mr(), column=0, sticky='news')

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
    mat_lb.grid(row=mr(), column=ucol, sticky='news')
    mat_show.grid(row=mr(), column=ucol, sticky='news')
    next_btn.grid(row=mr(), column=ucol, sticky='news')
    home_btn.grid(row=mr(), column=ucol, sticky='news')
    mat_lab.grid(row=mr(), column=ucol, sticky='news')


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
    if asset["current_func"] == "Quick Elementary":
        print("going to quick elem")
        transit("quickelem")
    elif asset["current_func"] == "Quick Inverse":
        print("going quick inv")
        transit("quickinv")
    elif asset["current_func"] != "":
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
    func_lb.grid(row=urow, column=ucol, sticky='news')
    next_btn.grid(row=mr(), column=ucol, sticky='news')
    back_btn.grid(row=mr(), column=ucol, sticky='news')
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
    row_lab.grid(row=urow, column=ucol, sticky='news')
    row_ent.grid(row=urow, column=ucol+1, sticky='news')
    col_lab.grid(row=mr(), column=ucol, sticky='news')
    col_ent.grid(row=urow, column=ucol+1, sticky='news')
    next_btn.grid(row=mr(), column=ucol, sticky='news')
    back_btn.grid(row=mr(), column=ucol, sticky='news')
    home_btn.grid(row=mr(), column=ucol, sticky='news')


def next1_fixedmat(re, ce):
    global root, scr, urow, ucol, stage, asset
    root.title("Matrix Calculator: Create Fixed Matrix Size >> Define Element")
    err = ""
    if re.get().isdigit() and ce.get().isdigit():
        r = int(re.get())
        c = int(ce.get())
        if r <= 0 or c <= 0:
            err = "Input cannot be lower than 1"
        if r > 15 or c > 15:
            err = "Input exceeded limitation (15x15 matrix), Use Quick function instead"

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
        i.grid(row=mr(), column=ucol, sticky='news')


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
    setting_btn = Button(root, text="Setting",
                         command=lambda: transit("setting"))

    hilabel.grid(row=urow, column=ucol, sticky='news')
    creatorlabel.grid(row=mr(), column=ucol, sticky='news')
    matter_btn.grid(row=mr(), column=ucol, sticky='news')
    matlist_btn.grid(row=mr(), column=ucol, sticky='news')
    matfunc_btn.grid(row=mr(), column=ucol, sticky='news')
    setting_btn.grid(row=mr(), column=ucol, sticky='news')
    exit_btn.grid(row=mr(), column=ucol, sticky='news')
    # working area open
    # test 2
    # master_frame = Frame(root, bd=3,
    #                      relief=RIDGE)
    # # master_frame = Frame(root, bg='Light Blue', bd=3,
    # #                      relief=RIDGE)
    # master_frame.grid(sticky=NSEW)
    # master_frame.columnconfigure(0, weight=1)

    # # label1 = Label(
    # #     master_frame, text='Frame1 Contendasdsadddsadasdasdasdasdasadsadsadasdasdadats')
    # # label1.grid(row=0, column=0, pady=5, sticky=NW)

    # frame1 = Frame(master_frame, bg='Green', bd=2, relief=FLAT)
    # frame1.grid(row=1, column=0, sticky=NW)

    # # cb_var1 = IntVar()
    # # checkbutton1 = Checkbutton(frame1, text='StartCheckBox', variable=cb_var1)
    # # checkbutton1.grid(row=0, column=0, padx=0, pady=0)

    # # label2 = Label(master_frame, text='Frame2 Contents')
    # # label2.grid(row=2, column=0, pady=5, sticky=NW)

    # # Create a frame for the canvas and scrollbar(s).
    # # frame2 = Frame(master_frame, bg='Red', bd=2, relief=FLAT)
    # # frame2.grid(row=3, column=0, sticky=NW)
    # frame2 = Frame(master_frame, bd=2, relief=FLAT)
    # frame2.grid(row=3, column=0, sticky=NW)

    # # Add a canvas in that frame.
    # canvas = Canvas(frame2, bg='Yellow')
    # canvas.grid(row=0, column=0)

    # # Create a vertical scrollbar linked to the canvas.
    # vsbar = Scrollbar(frame2, orient=VERTICAL, command=canvas.yview)
    # vsbar.grid(row=0, column=1, sticky=NS)
    # canvas.configure(yscrollcommand=vsbar.set)

    # # Create a horizontal scrollbar linked to the canvas.
    # hsbar = Scrollbar(frame2, orient=HORIZONTAL, command=canvas.xview)
    # hsbar.grid(row=1, column=0, sticky=EW)
    # canvas.configure(xscrollcommand=hsbar.set)

    # # Create a frame on the canvas to contain the grid of buttons.
    # buttons_frame = Frame(canvas)
    # ROWS, COLS = 40, 24  # Size of grid.
    # ROWS_DISP = 12  # Number of rows to display.
    # COLS_DISP = 16  # Number of columns to display.
    # # ROWS, COLS = 10, 6  # Size of grid.
    # # ROWS_DISP = 3  # Number of rows to display.
    # # COLS_DISP = 4  # Number of columns to display.
    # # , width=1000
    # hilabel = Label(
    #     buttons_frame, text="Welcome to Matrix Calculator")
    # creatorlabel = Label(
    #     buttons_frame, text="Created by Naphat and Samita")
    # matter_btn = Button(buttons_frame, text="Create Matrix",
    #                     command=lambda: transit("createmat"))
    # matlist_btn = Button(buttons_frame, text="Matrix List",
    #                      command=lambda: transit("matlist"))
    # matfunc_btn = Button(buttons_frame, text="Do Functions",
    #                      command=lambda: transit("matfunc"))
    # exit_btn = Button(buttons_frame, text="Quit",
    #                   command=exitProg)

    # hilabel.grid(row=urow, column=ucol)
    # creatorlabel.grid(row=mr(), column=ucol, sticky='news')
    # matter_btn.grid(row=mr(), column=ucol, sticky='news')
    # matlist_btn.grid(row=mr(), column=ucol, sticky='news')
    # matfunc_btn.grid(row=mr(), column=ucol, sticky='news')
    # exit_btn.grid(row=mr(), column=ucol, sticky='news')

    # # Add the buttons to the frame.
    # for i in range(1, ROWS+1):
    #     for j in range(1, COLS+1):
    #         button = Label(buttons_frame, padx=7, pady=7,
    #                        activebackground='orange', text='')
    #         button.grid(row=i, column=j, sticky='news')
    #         # button = Button(buttons_frame, padx=7, pady=7, relief=RIDGE,
    #         #                 activebackground='orange', text='[%d, %d]' % (i, j))
    #         # button.grid(row=i, column=j, sticky='news')

    # # Create canvas window to hold the buttons_frame.
    # canvas.create_window((0, 0), window=buttons_frame, anchor=NW)

    # buttons_frame.update_idletasks()  # Needed to make bbox info available.
    # bbox = canvas.bbox(ALL)  # Get bounding box of canvas with Buttons.

    # # Define the scrollable region as entire canvas with only the desired
    # # number of rows and columns displayed.
    # w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
    # dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
    # canvas.configure(scrollregion=bbox, width=dw, height=dh)

    # scr.append(canvas)
    # scr.append(buttons_frame)
    # scr.append(hsbar)
    # scr.append(vsbar)
    # scr.append(master_frame)
    # scr.append(frame1)
    # scr.append(frame2)
    # test
    # hilabel['yscrollcommand'] = set
    # creatorlabel['yscrollcommand'] = set
    # matter_btn['yscrollcommand'] = set
    # matlist_btn['yscrollcommand'] = set
    # matfunc_btn['yscrollcommand'] = set
    # exit_btn['yscrollcommand'] = set
    # test end
    # working area end
    scr.append(hilabel)
    scr.append(creatorlabel)
    scr.append(matter_btn)
    scr.append(exit_btn)
    scr.append(matlist_btn)
    scr.append(matfunc_btn)
    scr.append(setting_btn)


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
    elif stage == "inverse":
        show_inverse()
    elif stage == "setting":
        show_setting()
    elif stage == "quickelem_result":
        show_quickelem2()
    elif stage == "quickelem":
        show_quickelem()
    elif stage == "quickinv":
        show_quickinv()
    elif stage == "quickinv_result":
        show_quickinv2()


if __name__ == '__main__':
    root = Tk()
    # root.configure(bg="#DDDDDD")
    scr = []
    allmat = []
    urow = 0
    ucol = 0
    asset = {}
    asset["all_mat"] = []
    asset["all_func"] = ["Elementary", "Inverse",
                         "Quick Elementary", "Quick Inverse"]
    stage = "main"
    asset["o_set"] = 1
    asset["cons_set"] = 1
    asset["e_set"] = 1
    asset["t_set"] = 1
    asset["d_set"] = 1
    asset["cat_set"] = 1
    asset["rr_set"] = 1

    # frame = Frame(
    #     root,
    #     bg='#A8B9BF'
    # )

    # text_box = Text(
    #     root,
    #     height=13,
    #     width=32,
    #     font=(12)
    # )

    # text_box.grid(row=0, column=0)
    # text_box.config(bg='#D9D8D7')

    # sBar = Scrollbar(
    #     root,
    #     orient=VERTICAL
    # )

    # sBar.grid(row=0, column=1, sticky=NS)

    # text_box.config(yscrollcommand=set)
    # sBar.config(command=text_box.yview)
    summon()
    def_btn()
    def_mat()

    # test 5

    # test 4 with test

    # root.resizable(False, False)
    # root.title("Codeunderscored Scrollbar Widget Example")

    # # apply the grid layout
    # root.grid_columnconfigure(0, weight=1)
    # root.grid_rowconfigure(0, weight=1)

    # # create the text widget
    # text = Text(root, height=10)
    # text.grid(row=0, column=0, sticky='ew')

    # # create a scrollbar widget and set its command to the text widget
    # sBar = Scrollbar(root, orient='vertical', command=text.yview)
    # sBar.grid(row=0, column=1, sticky='ns')

    # #  communicate back to the scrollbar
    # text['yscrollcommand'] = set

    # root.mainloop()

    # test 3
    # main_frame = Frame(root)
    # main_frame.grid(fill=BOTH, expand=1)

    # # canvas
    # my_canvas = Canvas(main_frame)
    # my_canvas.grid(side=LEFT, fill=BOTH, expand=1)

    # # scrollbar
    # my_scrollbar = Scrollbar(
    #     main_frame, orient=VERTICAL, command=my_canvas.yview)
    # my_scrollbar.grid(side=RIGHT, fill=Y)

    # btn1 = Button(main_frame,
    #               text="Browse...",
    #               compound="left",
    #               fg="blue", width=22,
    #               font=("bold", 10),
    #               height=1,
    #               )

    # btn1.place(x=300, y=300)

    # configure the canvas
    # my_canvas.configure(yscrollcommand=my_scrollbar.set)
    # my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
    #     scrollregion=my_canvas.bbox("all")))

    # second_frame = Frame(my_canvas)

    # my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    # test

    # main_frame = Frame(root)
    # main_frame.pack(fill=BOTH, expand=1)

    # # canvas
    # my_canvas = Canvas(main_frame)
    # my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # # scrollbar
    # my_scrollbar = Scrollbar(
    #     main_frame, orient=VERTICAL, command=my_canvas.yview)
    # my_scrollbar.pack(side=RIGHT, fill=Y)

    # btn1 = Button(main_frame,
    #               text="Browse...",
    #               compound="left",
    #               fg="blue", width=22,
    #               font=("bold", 10),
    #               height=1,
    #               )

    # btn1.place(x=300, y=300)

    # # configure the canvas
    # my_canvas.configure(yscrollcommand=my_scrollbar.set)
    # my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
    #     scrollregion=my_canvas.bbox("all")))

    # second_frame = Frame(my_canvas)

    # my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # test 2

    # frame_main = Frame(root, bg="gray")
    # frame_main.grid(sticky='news')

    # # label1 = Label(frame_main, text="Label 1", fg="green")
    # # label1.grid(row=0, column=0, pady=(5, 0), sticky='nw')

    # # label2 = Label(frame_main, text="Label 2", fg="blue")
    # # label2.grid(row=1, column=0, pady=(5, 0), sticky='nw')

    # # label3 = Label(frame_main, text="Label 3", fg="red")
    # # label3.grid(row=3, column=0, pady=5, sticky='nw')

    # # Create a frame for the canvas with non-zero row&column weights
    # frame_canvas = Frame(frame_main)
    # frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
    # frame_canvas.grid_rowconfigure(0, weight=1)
    # frame_canvas.grid_columnconfigure(0, weight=1)
    # # Set grid_propagate to False to allow 5-by-5 buttons resizing later
    # frame_canvas.grid_propagate(False)

    # # Add a canvas in that frame
    # canvas = Canvas(frame_canvas, bg="yellow")
    # canvas.grid(row=0, column=0, sticky="news")

    # # Link a scrollbar to the canvas
    # vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    # vsb.grid(row=0, column=1, sticky='ns')
    # canvas.configure(yscrollcommand=vsb.set)

    # # Create a frame to contain the buttons
    # frame_buttons = Frame(canvas, bg="blue")
    # canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

    # # Add 9-by-5 buttons to the frame
    # rows = 9
    # columns = 5
    # buttons = [[Button() for j in range(columns)] for i in range(rows)]
    # for i in range(0, rows):
    #     for j in range(0, columns):
    #         buttons[i][j] = Button(frame_buttons, text=("%d,%d" % (i+1, j+1)))
    #         buttons[i][j].grid(row=i, column=j, sticky='news')

    # # Update buttons frames idle tasks to let tkinter calculate buttons sizes
    # frame_buttons.update_idletasks()

    # # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
    # first5columns_width = sum([buttons[0][j].winfo_width()
    #                           for j in range(0, 5)])
    # first5rows_height = sum([buttons[i][0].winfo_height()
    #                         for i in range(0, 5)])
    # frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
    #                     height=first5rows_height)

    # # Set the canvas scrolling region
    # canvas.config(scrollregion=canvas.bbox("all"))

    root.mainloop()
