from tkinter import *
from tkinter import messagebox
import time
import Frontend.main_interface
import Frontend.welcome
from tkinter import ttk
import Backend.database
import Model_class.department_register


class RegisterDepartment:
    def __init__(self, w):
        self.w = w
        self.w.geometry("1050x600+150+50")
        self.w.title("Department Register Form")
        self.w.configure(bg="white")

        self.db = Backend.database.Database()

        self.frame1 = Frame(self.w, bg="blue")
        self.frame1.place(x=10, y=60, width=1030, height=530)

        self.button_frame = Frame(self.frame1, bg="white")
        self.button_frame.place(x=0, y=370, width=1050, height=270)

        # Heading

        self.heading_label = Label(self.w, text="Department Registration Form", font=("Arial 30 bold"), bg="white")
        self.heading_label.place(x=250, y=5)

        self.dep_code_label = Label(self.frame1, text="Department Code:", font=("Arial 15 bold"), bg="blue", fg="white")
        self.dep_code_label.place(x=260, y=140)

        self.dep_code_entry = Entry(self.frame1, font=("Arial 10 bold"))
        self.dep_code_entry.place(x=450, y=145, width=270)

        self.dep_name_label = Label(self.frame1, text="Department Name:", font=("Arial 15 bold"), bg="blue", fg="white")
        self.dep_name_label.place(x=260, y=180)

        self.dep_name_entry = Entry(self.frame1, font=("Arial 10 bold"))
        self.dep_name_entry.place(x=450, y=185, width=270)
        # button

        self.reg_btn = Button(self.button_frame, text="ADD", font=("Arial 10 bold"), bg="blue", fg="white",
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
        self.date_time = Label(self.button_frame,
                               font=("Arial 10 bold"), bg="white")
        self.date_time.place(x=460, y=80)
        self.c_time_date()

    def c_time_date(self):
        self.c_time = time.strftime("%H:%M:%S")
        self.date = time.strftime("%Y/%m/%d")
        self.date_time.configure(text=f"TIME: {self.c_time}\n    DATE: {self.date}")
        self.date_time.after(100, self.c_time_date)

    def add(self):
        if self.dep_code_entry.get() != "" and self.dep_name_entry.get() != "":
            emp_obj = Model_class.department_register.DepartmentRegistration(self.dep_code_entry.get(),
                                                                             self.dep_name_entry.get())
            query = "insert into department (dep_code,name) values (%s,%s)"
            values = (emp_obj.get_code(), emp_obj.get_name())
            self.db.insert(query, values)
            messagebox.showinfo("Success", "Data Inserted Successfully")

        else:
            messagebox.showerror("Error", "All fields required")

    def clear_form(self):
        self.dep_code_entry.delete(0, END)
        self.dep_name_entry.delete(0, END)

    def main_interface(self):
        w = Tk()
        Frontend.main_interface.MainInterface(w)
        self.w.withdraw()

    def insert_field(self, a, b):
        self.dep_code_entry.insert(0, a)
        self.dep_name_entry.insert(0, b)






def w():
    w = Tk()
    RegisterDepartment(w)
    w.mainloop()


if __name__ == "__main__":
    w()
