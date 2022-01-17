class UserDisplayName:

    def __init__(self, login, fname, lname):
        self.login = login
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return str(self.fname) + " " + str(self.lname) + "(" + self.login + ")"


