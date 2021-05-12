from tkinter import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage


class QR_Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR_Generator | By Sam")
        self.root.resizable(False, False)  # both width and height non-resizable

        title = Label(
            self.root,
            text="   QR Code Generator",
            font=("times new roman", 40),
            bg="#053246",
            fg="white",
            anchor="w",
        ).place(x=0, y=0, relwidth=1)

        # ----------------------
        #  Employee Detail window
        # -----------------------
        self.var_emp_code = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_designation = StringVar()

        emp_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        emp_Frame.place(x=50, y=100, width=500, height=380)
        emp_title = Label(
            emp_Frame,
            text="Employee Details",
            font=("goudy old style", 20, "bold"),
            bg="#053242",
            fg="white",
        ).place(x=0, y=0, relwidth=1)

        lbl_empCode = Label(
            emp_Frame,
            text=" Employee Code",
            font=("times new roman", 15, "bold"),
            bg="white",
        ).place(x=20, y=60)
        lbl_name = Label(
            emp_Frame, text=" Name", font=("times new roman", 15, "bold"), bg="white"
        ).place(x=20, y=100)
        lbl_department = Label(
            emp_Frame,
            text=" Department",
            font=("times new roman", 15, "bold"),
            bg="white",
        ).place(x=20, y=140)
        lbl_designation = Label(
            emp_Frame,
            text=" Designation",
            font=("times new roman", 15, "bold"),
            bg="white",
        ).place(x=20, y=180)

        text_empCode = Entry(
            emp_Frame,
            font=("times new roman", 15),
            textvariable=self.var_emp_code,
            bg="lightyellow",
        ).place(x=200, y=60)
        text_name = Entry(
            emp_Frame,
            font=("times new roman", 15),
            textvariable=self.var_name,
            bg="lightyellow",
        ).place(x=200, y=100)
        text_department = Entry(
            emp_Frame,
            font=("times new roman", 15),
            textvariable=self.var_department,
            bg="lightyellow",
        ).place(x=200, y=140)
        text_designation = Entry(
            emp_Frame,
            font=("times new roman", 15),
            textvariable=self.var_designation,
            bg="lightyellow",
        ).place(x=200, y=180)

        btn_generate = Button(
            emp_Frame,
            text="Generate QR",
            command=self.generate,
            font=("times new roman", 18, "bold"),
            bg="blue",
            fg="white",
        ).place(x=90, y=250, width=180, height=30)
        btn_clear = Button(
            emp_Frame,
            text="Clear",
            command=self.clear,
            font=("times new roman", 18, "bold"),
            bg="#607d8b",
            fg="white",
        ).place(x=280, y=250, width=120, height=30)

        # ----we need a msg which will be changing depending upon the user's action --relwidth = 1 means text would come at center
        self.msg = "QR Generated Successfully !!!"
        self.lbl_msg = Label(
            emp_Frame,
            text=self.msg,
            font=("times new roman", 15),
            bg="white",
            fg="green",
        )
        self.lbl_msg.place(x=0, y=310, relwidth=1)

        # defined in double line because for entire class we've to use

        # ----------------------
        #  QR  Window
        # -----------------------
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        qr_Frame.place(x=600, y=100, width=250, height=380)
        emp_title = Label(
            qr_Frame,
            text="Employee QR Code",
            font=("goudy old style", 20, "bold"),
            bg="#053242",
            fg="white",
        ).place(x=0, y=0, relwidth=1)

        # -- can put the image either on the button or on the label

        self.qr_code = Label(
            qr_Frame,
            text="QR Code \nNot Available",
            font=("times new roman", 15),
            bg="#3f51bf",
            fg="white",
            bd=1,
            relief=RIDGE,
        )

        self.qr_code.place(x=35, y=100, width=180, height=180)

    def generate(self):
        # print(self.var_emp_code.get(),self.var_name.get(),self.var_department.get(),self.var_designation.get())
        if (
            self.var_department.get() == ""
            or self.var_designation.get() == ""
            or self.var_emp_code.get() == ""
            or self.var_name.get() == ""
        ):
            self.msg = "Fill All The Fields First !!!"
            self.lbl_msg.config(text=self.msg, fg="red")
        else:

            # fetch the qrdata that would be a tuple and pass a fstring

            qr_data = f"Employee ID : {self.var_emp_code.get()}\n Employee Name : {self.var_name.get()}\n Department : {self.var_department.get()}\n Designation : {self.var_designation.get()}"

            # make the qrcode of your data
            qr_code = qrcode.make(qr_data)
            # now qrcode will contain an image object
            print(qr_code)

            # resize the img
            qr_code = resizeimage.resize_cover(qr_code, [180, 180])

            qr_code.save("Data/Emp_" + str(self.var_emp_code.get()) + ".png")
            # === update the qr code image
            # self.im = ImageTk.PhotoImage(qr_code)
            self.im = ImageTk.PhotoImage(
                file="Data/Emp_" + str(self.var_emp_code.get()) + ".png"
            )

            # apply this image to image label already defined

            self.qr_code.config(
                image=self.im
            )  # we have given height and width =180 for qr_codeWindow so resize them image

            # -------updating the notifications------------
            self.msg = "QR Generated Successfully :)"
            self.lbl_msg.config(text=self.msg, fg="green")

    def clear(self):
        self.var_emp_code.set(" ")
        self.var_name.set(" ")
        self.var_department.set(" ")
        self.var_designation.set(" ")
        self.msg = ""
        self.lbl_msg.config(text=self.msg)

        self.qr_code.config(image="")


# -----------------------------
# make object for tk and class
# -----------------------------

root = Tk()
obj = QR_Generator(root)

root.mainloop()  # for a static tk window
