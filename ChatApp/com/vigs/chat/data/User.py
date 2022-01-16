class User:

    def __init__(self, login, fname, lname, password):
        self.login = login
        self.fname = fname
        self.lname = lname
        self.password = password


    def __str__(self):
        return "User[login: " + self.login + ", fname: " + self.fname + ", lname: " + self.lname + "]"

