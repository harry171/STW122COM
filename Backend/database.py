import mysql.connector


class Database:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", port=3306, user="root", password="",
                                           database = "employeesystem")
        self.cur = self.con.cursor()

    def __del__(self):
        try:
            if self.cur:
                self.cur.close()
            if self.con:
                self.con.close()

        except BaseException as msg:
            pass

    def select1(self, query, values):
        self.cur.execute(query, values)
        d = self.cur.fetchall()
        self.con.commit()
        return d

    def insert(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()

    def select(self, query):
        self.cur.execute(query)
        d = self.cur.fetchall()
        self.con.commit()
        return d

    def update(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()

    def delete(self, query, values):
        self.cur.execute(query, values)
        self.con.commit()
git

Database()
