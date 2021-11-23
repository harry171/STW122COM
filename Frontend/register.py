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

    def c_time_date(self):
        self.c_time = time.strftime("%H:%M:%S")
        self.date = time.strftime("%Y/%m/%d")
        self.date_time.configure(text=f"TIME: {self.c_time}\n    DATE: {self.date}")
        self.date_time.after(100, self.c_time_date)

    def add(self):
        if self.username_entry.get() != "" and self.email_entry.get() != "" and self.password_entry.get() != "" and \
                self.full_name_entry.get() != "" and self.d_o_b_entry.get() != "" and self.gender_entry.get() != "" and \
                self.address_entry.get() != "" and self.contact_entry.get() != "" and self.department_entry.get():
            emp_obj = Model_class.register.Registration(self.username_entry.get(),
                                                        self.email_entry.get(),
                                                        self.password_entry.get(),
                                                        self.full_name_entry.get(),
                                                        self.d_o_b_entry.get(),
                                                        self.gender_entry.get(),
                                                        self.address_entry.get(),
                                                        self.contact_entry.get(),
                                                        self.department_entry.get())
            query = "insert into employee (username,email,password,name,gender,dob,address,contact,department) values " \
                    "(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (emp_obj.get_username(), emp_obj.get_email(), emp_obj.get_password(), emp_obj.get_name(),
                      emp_obj.get_gender(), emp_obj.get_dob(), emp_obj.get_address(), emp_obj.get_contact(),
                      emp_obj.get_department())
            self.db.insert(query, values)
            messagebox.showinfo("Success", "Data Inserted Successfully")

        else:
            messagebox.showerror("Error", "All field required")

    def clear_form(self):
        self.username_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.c_password_entry.delete(0, END)
        self.gender_entry.current(0)
        self.address_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.d_o_b_entry.delete(0, END)
        self.department_entry.current(0)
        self.full_name_entry.delete(0, END)

    def clear_dob(self, events):
        self.d_o_b_entry.delete(0, END)
        self.d_o_b_entry.configure(fg="black")

    def main_interface(self):
        w = Tk()
        Frontend.main_interface.MainInterface(w)
        self.w.withdraw()


class ViewEmployee:
    data = []

    def __init__(self, w):
        self.w = w
        self.w.geometry("1050x600+150+50")
        self.w.title("View Employee")
        self.w.configure(bg="blue")
        self.db = Backend.database.Database()

        self.heading = Label(self.w, text="VIEWING ALL EMPLOYEES", font=("Arial 25 bold"), bg="blue", fg="white")
        self.heading.place(x=280, y=10)

        self.search_label = Label(self.w, text="SEARCH", font=("Arial 15 bold"), bg="blue", fg="white")
        self.search_label.place(x=100, y=70)

        self.search_entry = Entry(self.w, font=("Arial 10 bold"))
        self.search_entry.place(x=200, y=75, width=200)

        self.search_btn = Button(self.w, text ="SEARCH", font="Arial 8 bold", bg="blue", fg="white",
                                 cursor="hand2", relief=GROOVE, bd=5, activebackground="white",
                                 command=self.searching)
        self.search_btn.place(x= 430,y=70)

        self.view_btn = Button(self.w, text="VIEW ALL", font=("Arial 8 bold"), bg="blue", fg="white",
                               cursor="hand2", relief=GROOVE, bd=5, activebackground="white",
                               command=self.viewall)
        self.view_btn.place(x=960, y=70)

        self.sort_label = Label(self.w, text="SORT", font=("Arial 15 bold"), bg="blue", fg="white")
        self.sort_label.place(x=530, y=70)

        self.sort = ttk.Combobox(self.w, state="readonly")
        self.sort['values'] = ['By ID']
        self.sort.current(0)
        self.sort.place(x=600, y=75)

        self.sort_t = ttk.Combobox(self.w, state="readonly")
        self.sort_t['values'] = ['Increasing', "Decreasing"]
        self.sort_t.bind('<<ComboboxSelected>>',self.sorting)
        self.sort_t.current(0)
        self.sort_t.place(x=750, y=75, width=200)

        self.update_btn = Button(self.w, text="UPDATE", font=("Arial 10 bold"), bg="blue", fg="white",
                                 cursor="hand2", relief=GROOVE, bd=5, activebackground="white",
                                 command=self.update)
        self.update_btn.place(x=360, y=530, width=100)

        self.delete_btn = Button(self.w, text="DELETE", font=("Arial 10 bold"), bg="blue", fg="white",
                                 cursor="ha"
                                        "nd2", relief=GROOVE, bd=5, activebackground="white", command=self.delete)
        self.delete_btn.place(x=490, y=530, width=100)

        self.back_btn = Button(self.w, text="BACK", font=("Arial 10 bold"), bg="blue", fg="white",
                               cursor="ha"
                                      "nd2", relief=GROOVE, bd=5, activebackground="white", command=self.back)
        self.back_btn.place(x=620, y=530, width=100)

        # ==================TreeView Frame=================
        self.table_frame = Frame(self.w, bd=4, relief=RIDGE, bg="white")
        self.table_frame.place(x=10, y=120, width=1030, height=400)

        scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.emp_tree = ttk.Treeview(self.table_frame,
                                     columns=(
                                         "EMPLOYEE ID", "EMPLOYEE NAME", "EMAIL", "DOB", "GENDER", "ADDRESS", "CONTACT",
                                         "DEPARTMENT"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.emp_tree.xview)
        scroll_y.config(command=self.emp_tree.yview)

        # ==========================TreeView Heading====================
        self.emp_tree.heading("EMPLOYEE ID", text="EMPLOYEE ID")
        self.emp_tree.heading("EMPLOYEE NAME", text="EMPLOYEE NAME")
        self.emp_tree.heading("EMAIL", text="EMAIL")
        self.emp_tree.heading("DOB", text="DOB")
        self.emp_tree.heading("GENDER", text="GENDER")
        self.emp_tree.heading("ADDRESS", text="ADDRESS")
        self.emp_tree.heading("CONTACT", text="CONTACT")
        self.emp_tree.heading("DEPARTMENT", text="DEPARTMENT")
        self.emp_tree["show"] = "headings"

        # ==========================TreeView Column====================
        self.emp_tree.column("EMPLOYEE ID", width=150)
        self.emp_tree.column("EMPLOYEE NAME", width=150)
        self.emp_tree.column("EMAIL", width=200)
        self.emp_tree.column("ADDRESS", width=150)
        self.emp_tree.column("GENDER", width=150)
        self.emp_tree.column("CONTACT", width=150)
        self.emp_tree.column("DOB", width=150)
        self.emp_tree.column("DEPARTMENT", width=150)
        self.emp_tree.pack(fill=BOTH, expand=1)
        self.viewall()

    def viewall(self):
        try:
            query = "select * from employee"
            rows = self.db.select(query)
            self.emp_tree.delete(*self.emp_tree.get_children())
            for i in rows:
                val = [i[0], i[4], i[2], i[6], i[5], i[7], i[8], i[9]]
                self.emp_tree.insert('', END, values=val)

        except:
            pass









def w():
    w = Tk()
    Register(w)
    w.mainloop()


if __name__ == "__main__":
    w()
