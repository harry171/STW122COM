from tkinter import *
from tkinter import messagebox
import time
import Frontend.register
import Frontend.welcome
import Backend.database


class Login:
    def __init__(self, w):
        self.w = w
        self.w.geometry("1050x600+150+50")
        self.w.title("Employee Login Form")
        self.w.configure(bg="white")

        self.db = Backend.database.Database()

        self.frame1 = Frame(self.w, bg="blue")
        self.frame1.place(x=10, y=60, width=1030, height=530)

        self.button_frame = Frame(self.frame1, bg="white")
        self.button_frame.place(x=0, y=370, width=1050, height=270)

        # Heading

        self.heading_label = Label(self.w, text="Employee Login Form", font=("Arial 30 bold"), bg="white")
        self.heading_label.place(x=310, y=5)

        self.username_label = Label(self.frame1, text="Username:", font=("Arial 15 bold"), bg="blue", fg="white")
        self.username_label.place(x=300, y=140)

        self.username_entry = Entry(self.frame1, font=("Arial 10 bold"))
        self.username_entry.place(x=420, y=145, width=300)

        self.password_label = Label(self.frame1, text="Password:", font=("Arial 15 bold"), bg="blue", fg="white")
        self.password_label.place(x=300, y=200)

        self.password_entry = Entry(self.frame1, font=("Arial 10 bold"), fg="grey")
        self.password_entry.place(x=420, y=205, width=300)
        self.password_entry.insert(0, "Enter your password here......")

        self.password_entry.bind("<1>", self.clear_password)

        # button

        self.login_btn = Button(self.button_frame, text="LOGIN", font=("Arial 10 bold"), bg="blue", fg="white",
                                cursor="hand2", relief=GROOVE, bd=5, activebackground="white"
                                , command=self.check_details)
        self.login_btn.place(x=360, y=10, width=100)

        self.reg_btn = Button(self.button_frame, text="REGISTER", font=("Arial 10 bold"), bg="blue", fg="white",
                              cursor="hand2", relief=GROOVE, bd=5, activebackground="white", command=self.employee_reg)
        self.reg_btn.place(x=600, y=10, width=100)

        self.clr_btn = Button(self.button_frame, text="CLEAR FORM", font=("Arial 10 bold"), bg="blue", fg="white",
                              cursor="hand2", relief=GROOVE, bd=5, activebackground="white", command=self.clear_form)
        self.clr_btn.place(x=480, y=10, width=100)

        # current time
        self.date_time = Label(self.w,
                               font=("Arial 10 bold"), bg="white")
        self.date_time.place(x=860, y=15)
        self.c_time_date()

    def c_time_date(self):
        self.c_time = time.strftime("%H:%M:%S")
        self.date = time.strftime("%Y/%m/%d")
        self.date_time.configure(text=f"TIME: {self.c_time}\n    DATE: {self.date}")
        self.date_time.after(100, self.c_time_date)

    def check_details(self):
        try:
            query = "select * from employee where username = %s"
            values = (self.username_entry.get(),)
            rows = self.db.select1(query, values)

            for i in rows:
                self.user = i[1]
                self.password = i[3]

            if self.username_entry.get() != "" and self.password_entry.get() != "":
                if self.user == self.username_entry.get() and self.password == self.password_entry.get():
                    messagebox.showinfo("Success", f"You are successfully logged in {self.user}")
                    self.login_complete()
                else:
                    messagebox.showerror("Error", "Invalid username or password")
            elif self.username_entry.get() == "":
                messagebox.showerror("required", "The field is required")

            elif self.password_entry.get() == "":
                messagebox.showerror("required", "The field is required")

            else:
                pass

        except:
            pass

    def clear_form(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def clear_password(self, events):
        self.password_entry.delete(0, END)
        self.password_entry.configure(fg="black")

    def employee_reg(self):
        w = Tk()
        Frontend.register.Register(w)
        self.w.withdraw()

    def login_complete(self):
        w = Tk()
        Frontend.welcome.Welcome(w)
        self.w.withdraw()


def w():
    w = Tk()
    Login(w)
    w.mainloop()


if __name__ == "__main__":
    w()
