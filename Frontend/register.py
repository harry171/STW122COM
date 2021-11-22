from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import Frontend.main_interface
import Frontend.welcome
import Model_class.register
import Backend.database


class Register:
    def __init__(self, w):
        self.w = w
        self.w.geometry("1050x600+150+50")
        self.w.title("Employee Register Form")
        self.w.configure(bg="white")

        self.db = Backend.database.Database()

        self.frame1 = Frame(self.w, bg="blue")
        self.frame1.place(x=10, y=60, width=1030, height=530)

        self.button_frame = Frame(self.frame1, bg="white")
        self.button_frame.place(x=0, y=470, width=1050, height=270)

        # Heading

        self.heading_label = Label(self.w, text="Employee Registration Form", font=("Arial 30 bold"), bg="white")
        self.heading_label.place(x=250, y=5)

        self.username_label = Label(self.frame1, text="Username:", font=("Arial 15 bold"), bg="blue", fg="white")
        self.username_label.place(x=300, y=40)

        self.username_entry = Entry(self.frame1, font=("Arial 10 bold"))
        self.username_entry.place(x=420, y=45, width=300)

        self.email_label = Label(self.frame1, text="Email:", font=("Arial 15 bold"), bg="blue", fg="white")
        self.email_label.place(x=300, y=80)

        self.email_entry = Entry(self.frame1, font=("Arial 10 bold"))
        self.email_entry.place(x=420, y=85, width=300)

        self.password_label = Label(self.frame1, text="Password:", font=("Arial 15 bold"), bg="blue", fg="white")
        self.password_label.place(x=300, y=120)

        self.password_entry = Entry(self.frame1, font=("Arial 10 bold"))
        self.password_entry.place(x=420, y=125, width=300)

        self.c_password_label = Label(self.frame1, text="Confirm Password:", font=("Arial 15 bold"), bg="blue",
                                      fg="white")
        self.c_password_label.place(x=300, y=160)

        self.c_password_entry = Entry(self.frame1, font=("Arial 10 bold"))
        self.c_password_entry.place(x=500, y=165, width=220)

        self.full_name_label = Label(self.frame1, text="Full Name:", font=("Arial 15 bold"), bg="blue", fg="white")
        self.full_name_label.place(x=300, y=200)

        self.full_name_entry = Entry(self.frame1, font="Arial 10 bold")
        self.full_name_entry.place(x=420, y=205, width=300)

        self.gender_label = Label(self.frame1, text="Gender:", font=("Arial 15 bold"), bg="blue", fg="white")
        self.gender_label.place(x=300, y=240)

        self.gender_entry = ttk.Combobox(self.frame1, font="Arial 10 bold", state="readonly")
        self.gender_entry['values']=['Male','Female','I will not say']
        self.gender_entry.current(0)
        self.gender_entry.place(x=420, y=245, width=300)

        self.d_o_b_label = Label(self.frame1, text="DOB:", font=("Arial 15 bold"), bg="blue", fg="white")
        self.d_o_b_label.place(x=300, y=280)

        self.d_o_b_entry = Entry(self.frame1, font=("Arial 10 bold"))
        self.d_o_b_entry.place(x=420, y=285, width=300)
        self.d_o_b_entry.insert(0, "yyyy/mm/dd")
        self.d_o_b_entry.bind("<1>", self.clear_dob)
        self.d_o_b_entry.configure(fg="grey")

        self.address_label = Label(self.frame1, text="Address:", font=("Arial 15 bold"), bg="blue", fg="white")
        self.address_label.place(x=300, y=320)

        self.address_entry = Entry(self.frame1, font=("Arial 10 bold"))
        self.address_entry.place(x=420, y=325, width=300)

        self.contact_label = Label(self.frame1, text="Contact:", font=("Arial 15 bold"), bg="blue", fg="white")
        self.contact_label.place(x=300, y=360)

        self.contact_entry = Entry(self.frame1, font=("Arial 10 bold"))
        self.contact_entry.place(x=420, y=365, width=300)

        self.department_label = Label(self.frame1, text="Department:", font=("Arial 15 bold"), bg="blue", fg="white")
        self.department_label.place(x=300, y=400)

        try:
            query = "select * from department"
            lis= self.db.select(query)
            self.dep_list = []
            for i in lis:
                self.dep_list.append(i[2])

            self.department_entry = ttk.Combobox(self.frame1, font=("Arial 10 bold"), state='readonly')
            self.department_entry['values'] = self.dep_list
            self.department_entry.current(0)
            self.department_entry.place(x=440, y=405, width=280)

        except:
            messagebox.showinfo("Not any value","Please register department")

        # button

        self.reg_btn = Button(self.button_frame, text="REGISTER", font=("Arial 10 bold"), bg="blue", fg="white",
                              cursor="hand2", relief=GROOVE, bd=5, activebackground="white", command=self.add)
        self.reg_btn.place(x=360, y=10, width=100)

        self.clr_btn = Button(self.button_frame, text="CLEAR FORM", font=("Arial 10 bold"), bg="blue", fg="white",
                              cursor="hand2", relief=GROOVE, bd=5, activebackground="white", command=self.clear_form)
        self.clr_btn.place(x=480, y=10, width=100)

        self.back_btn = Button(self.button_frame, text="BACK", font=("Arial 10 bold"), bg="blue", fg="white",
                               cursor="hand2", relief=GROOVE, bd=5, activebackground="white",
                               command=self.main_interface)
        self.back_btn.place(x=600, y=10, width=100)

        # current time
        self.date_time = Label(self.w,
                               font=("Arial 10 bold"), bg="white")
        self.date_time.place(x=890, y=15)
        self.c_time_date()











def w():
    w = Tk()
    Register(w)
    w.mainloop()


if __name__ == "__main__":
    w()
