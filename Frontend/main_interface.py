from tkinter import *
import time
import Frontend.login
import Frontend.register
import Frontend.department_register


class MainInterface:
    def __init__(self, w):
        self.w = w
        self.w.geometry("1050x600+150+50")
        self.w.title("Main Interface")
        self.w.configure(bg="white")

        self.frame1 = Frame(self.w, bg="blue")
        self.frame1.place(x=10, y=60, width=1030, height=530)

        # Heading

        self.heading_label = Label(self.w, text="You Are Welcome", font=("Arial 30 bold"), bg="white")
        self.heading_label.place(x=380, y=5)

        # button

        self.login_btn = Button(self.frame1, text="EMPLOYEE LOGIN", font=("Arial 10 bold"), bg="blue", fg="white",
                               cursor="hand2", relief=GROOVE, bd=5, activebackground="white", command = self.login)
        self.login_btn.place(x=210, y=250, width=200)

        self.reg_btn = Button(self.frame1,text = "EMPLOYEE REGISTER", font=("Arial 10 bold"), bg = "blue",fg = "white",
                              cursor = "hand2",relief = GROOVE,bd = 5, activebackground = "white"
                              ,command = self.employee_reg)
        self.reg_btn.place(x=650, y = 250, width = 200)

        self.reg_dep_btn = Button(self.frame1, text="DEPARTMENT REGISTER", font=("Arial 10 bold"), bg="blue", fg="white",
                              cursor="hand2", relief=GROOVE, bd=5, activebackground="white"
                                  ,command = self.department_reg)
        self.reg_dep_btn.place(x=430, y=250, width = 200)


        # current time
        self.date_time = Label(self.w,
                               font=("Arial 10 bold"),bg = "white")
        self.date_time.place(x = 860 , y = 15 )
        self.c_time_date()

    def c_time_date(self):
        self.c_time = time.strftime("%H:%M:%S")
        self.date = time.strftime("%Y/%m/%d")
        self.date_time.configure(text = f"TIME: {self.c_time}\n    DATE: {self.date}")
        self.date_time.after(100,self.c_time_date)

    def login(self):
        w = Tk()
        Frontend.login.Login(w)
        self.w.withdraw()

    def department_reg(self):
        w = Tk()
        Frontend.department_register.RegisterDepartment(w)
        self.w.withdraw()

    def employee_reg(self):
        w = Tk()
        Frontend.register.Register(w)
        self.w.withdraw()

def w():
    w = Tk()
    MainInterface(w)
    w.mainloop()


if __name__ == "__main__":
    w()
