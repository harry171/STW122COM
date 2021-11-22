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


class ViewDepartment:
    data = []

    def __init__(self, w):
        self.w = w
        self.w.geometry("1050x600+150+50")
        self.w.title("View Department")
        self.w.configure(bg="blue")
        self.db = Backend.database.Database()

        self.heading = Label(self.w, text="VIEWING ALL DEPARTMENT", font=("Arial 25 bold"), bg="blue", fg="white")
        self.heading.place(x=240, y=10)

        self.search_label = Label(self.w, text="SEARCH", font=("Arial 15 bold"), bg="blue", fg="white")
        self.search_label.place(x=100, y=70)

        self.search_entry = Entry(self.w, font=("Arial 10 bold"))
        self.search_entry.place(x=200, y=75, width=200)

        self.search_btn = Button(self.w, text="SEARCH", font="Arial 8 bold", bg="blue", fg="white",
                                 cursor="hand2", relief=GROOVE, bd=5, activebackground="white",
                                 command=self.searching)
        self.search_btn.place(x=430, y=70)

        self.sort_label = Label(self.w, text="SORT", font=("Arial 15 bold"), bg="blue", fg="white")
        self.sort_label.place(x=530, y=70)

        self.sort = ttk.Combobox(self.w, state="readonly")
        self.sort['values'] = ['By Code']
        self.sort.current(0)
        self.sort.place(x=600, y=75)

        self.sort_t = ttk.Combobox(self.w, state="readonly")
        self.sort_t['values'] = ['Increasing', "Decreasing"]
        self.sort_t.current(0)
        self.sort_t.bind('<<ComboboxSelected>>',self.sorting)
        self.sort_t.place(x=750, y=75, width=200)

        self.view_btn = Button(self.w, text="VIEW ALL", font=("Arial 8 bold"), bg="blue", fg="white",
                               cursor="hand2", relief=GROOVE, bd=5, activebackground="white",
                               command=self.viewall)
        self.view_btn.place(x=960, y=70)

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
        self.dep_tree = ttk.Treeview(self.table_frame,
                                     columns=(
                                         "DEPARTMENT ID", "DEPARTMENT CODE", "DEPARTMENT NAME"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.dep_tree.xview)
        scroll_y.config(command=self.dep_tree.yview)

        # ==========================TreeView Heading====================
        self.dep_tree.heading("DEPARTMENT ID", text="DEPARTMENT ID")
        self.dep_tree.heading("DEPARTMENT CODE", text="DEPARTMENT CODE")
        self.dep_tree.heading("DEPARTMENT NAME", text="DEPARTMENT NAME")
        self.dep_tree["show"] = "headings"

        # ==========================TreeView Column====================
        self.dep_tree.column("DEPARTMENT ID", width=50)
        self.dep_tree.column("DEPARTMENT CODE", width=150)
        self.dep_tree.column("DEPARTMENT NAME", width=150)
        self.dep_tree.pack(fill=BOTH, expand=1)
        self.viewall()

    def viewall(self):
        try:
            query = "select * from department"
            rows = self.db.select(query)
            self.dep_tree.delete(*self.dep_tree.get_children())
            for i in rows:
                self.dep_tree.insert('', END, values=i)

        except:
            pass

    def update(self):
        val = self.dep_tree.focus()
        val_items = self.dep_tree.item(val)
        values = val_items['values']
        ViewDepartment.data.clear()
        ViewDepartment.data.append(values)

        w = Tk()
        UpdateDepartment(w)
        self.w.withdraw()

    def searching(self):
        ent = self.search_entry.get()
        if ent != "":
            try:
                lis = []
                for i in self.dep_tree.get_children():
                    a = self.dep_tree.item(i)['values'][0]
                    lis.append(a)
                print(f"list = {lis}")
                search = self.linearsearch(lis, int(self.search_entry.get()))
                print(f"search = {search}")
                if search:
                    messagebox.showinfo("Success", "Found")
                    query = "select * from department where id = %s"
                    values = (search,)
                    a = self.db.select1(query, values)
                    self.dep_tree.delete(*self.dep_tree.get_children())
                    for i in a:
                        self.dep_tree.insert('', END, values=i)

                else:
                    messagebox.showerror("failed", "Error, Not found")

            except:
                messagebox.showerror("Not Found", "Error, Not found")

    def sorting(self,events):
        if self.sort.get() == "By Code" and self.sort_t.get() == "Increasing":
            query = "select * from department;"
            data = self.db.select(query)
            sort_val = []
            for values in data:
                sort_val.append(values)
            sorted_val = self.b_sort_a(sort_val)
            if len(sorted_val) != 0:
                messagebox.showinfo("Done","Sorted increasing order")
                self.dep_tree.delete(*self.dep_tree.get_children())
                for i in sorted_val:
                    self.dep_tree.insert('', END, values=i)

        elif self.sort.get() == "By Code" and self.sort_t.get() == "Decreasing":
            query = "select * from department;"
            data = self.db.select(query)
            sort_val = []
            for values in data:
                sort_val.append(values)
            sorted_val = self.b_sort_d(sort_val)
            if len(sorted_val) != 0:
                messagebox.showinfo("Done","Sorted Decreasing order")
                self.dep_tree.delete(*self.dep_tree.get_children())
                for i in sorted_val:
                    self.dep_tree.insert('', END, values=i)


    def b_sort_a(self, lis):
        for j in range(len(lis) - 1):
            for i in range(len(lis) - 1):
                if lis[i] > lis[i + 1]:
                    lis[i], lis[i + 1] = lis[i + 1], lis[i]
        return lis

    def b_sort_d(self, lis):
        for j in range(len(lis) - 1):
            for i in range(len(lis) - 1):
                if lis[i] < lis[i + 1]:
                    lis[i], lis[i + 1] = lis[i + 1], lis[i]
        return lis

    def linearsearch(self, lis, x):
        for i in range(len(lis)):
            if int(lis[i]) == int(x):
                # print(lis[i])
                return lis[i]
        return False

    def delete(self):
        val = self.dep_tree.focus()
        val_items = self.dep_tree.item(val)
        values = val_items['values']
        delete = values[0]
        if delete >= 1:
            query = "delete from department where id = %s"
            values = (delete,)
            self.db.delete(query, values)
            messagebox.showinfo("Success", "Data delete successfully")
            self.viewall()

        else:
            messagebox.showerror("error", "There is some error deleting the record")

    def back(self):
        w = Tk()
        Frontend.welcome.Welcome(w)
        self.w.withdraw()


class UpdateDepartment(RegisterDepartment):
    def __init__(self, w):
        super().__init__(w)
        self.data = ViewDepartment.data[0]
        self.dep_code_entry.insert(0, self.data[1])
        self.dep_name_entry.insert(0, self.data[2])
        self.heading_label.configure(text="Department Update Form")
        self.heading_label.place(x=300, y=5)
        self.reg_btn.configure(text="UPDATE")
        self.reg_btn.configure(command=self.update)
        self.back_btn.configure(command=self.back)

    def back(self):
        w = Tk()
        ViewDepartment(w)
        self.w.withdraw()

    def update(self):
        try:
            query = "update department set dep_code = %s , name = %s where id = %s"
            values = (self.dep_code_entry.get(), self.dep_name_entry.get(), self.data[0])
            self.db.update(query, values)

            messagebox.showinfo("Success", f"Department ID  {self.data[0]} Updated Successfully")

        except BaseException as err:
            messagebox.showerror("error", f"{err}")


def w():
    w = Tk()
    RegisterDepartment(w)
    w.mainloop()


if __name__ == "__main__":
    w()
