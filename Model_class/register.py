class Registration:
    def __init__(self, username, email, password, name, dob, gender, address, contact, department):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.dob = dob
        self.gender = gender
        self.address = address
        self.contact = contact
        self.department=department

    def set_username(self, username):
        self.username = username

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def set_name(self, f_name):
        self.name = f_name

    def set_dob(self, dob):
        self.dob = dob

    def set_gender(self, gender):
        self.gender = gender

    def set_address(self, address):
        self.address = address

    def set_contact(self, contact):
        self.contact = contact

    def set_department(self, department):
        self.department = department

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_gender(self):
        return self.gender

    def get_address(self):
        return self.address

    def get_contact(self):
        return self.contact

    def get_department(self):
        return self.department
