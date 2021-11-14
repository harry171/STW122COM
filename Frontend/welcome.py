from tkinter import *
import time
import Frontend.department_register
import Frontend.register


class Welcome:
    def __init__(self, w):
        self.w = w
        self.w.geometry("1050x600+150+50")
        self.w.title("Welcome Page")
        self.w.configure(bg="white")

        self.frame1 = Frame(self.w, bg="blue")
        self.frame1.place(x=10, y=60, width=1030, height=530)

        # Heading

        self.heading_label = Label(self.w, text="Welcome Page", font=("Arial 30 bold"), bg="white")
        self.heading_label.place(x=380, y=5)

        # button

        self.view_emp = Button(self.frame1, text="VIEW EMPLOYEE", font=("Arial 10 bold"), bg="blue", fg="white",
                               cursor="hand2", relief=GROOVE, bd=5, activebackground="white",command = self.view_employee)
        self.view_emp.place(x=410, y=200, width=200)

        self.view_dep_btn = Button(self.frame1, text="VIEW DEPARTMENT", font=("Arial 10 bold"), bg="blue", fg="white",
                              cursor="hand2", relief=GROOVE, bd=5, activebackground="white",command = self.view_deparment)
        self.view_dep_btn.place(x=410, y=250, width = 200)


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

    def view_deparment(self):
        w = Tk()
        Frontend.department_register.ViewDepartment(w)
        self.w.withdraw()

    def view_employee(self):
        w = Tk()
        Frontend.register.ViewEmployee(w)
        self.w.withdraw()


def w():
    w = Tk()
    Welcome(w)
    w.mainloop()


if __name__ == "__main__":
    w()
