import tkinter
from com.vigs.chat.ui.ChatWindow import ChatWindow
from com.vigs.chat.Application import Application

class LoginWindow:

    def __init__(self, application:Application):
        self.application = application
        self.build()

    def build(self):
        self.root = tkinter.Tk()
        self.root.title("Login")
        self.loginIdLabel = tkinter.Label(self.root, text="Login")
        self.passwordLabel = tkinter.Label(self.root, text="Password")
        self.txtLogin = tkinter.Entry(self.root, width=30)
        self.txtPassword = tkinter.Entry(self.root, width=30)
        self.btnLogin = tkinter.Button(self.root, text="Login")
        self.btnCancel = tkinter.Button(self.root, text="Cancel")

        self.loginIdLabel.grid(row=0, column=0, sticky=tkinter.NSEW)
        self.passwordLabel.grid(row=1, column=0, sticky=tkinter.NSEW)
        self.txtLogin.grid(row=0, column=1, columnspan=2, sticky=tkinter.NSEW)
        self.txtPassword.grid(row=1, column=1, columnspan=2, sticky=tkinter.NSEW)
        self.btnLogin.grid(row=2, column=1, sticky=tkinter.NSEW)
        self.btnCancel.grid(row=2, column=2, sticky=tkinter.NSEW)

        self.bindEventHandlers()

        self.txtLogin.configure(text="svig")
        self.txtPassword.config(text="vig")

    def bindEventHandlers(self):
        self.root.bind("<Escape>", self.exit)
        self.root.bind("<Return>", self.submit)

    def launch(self):
        self.root.mainloop()

    def exit(self, event):
        quit()

    def submit(self, event):
        self.root.withdraw()
        self.application.loginUser(login=self.txtLogin.get(), password=self.txtPassword.get())
        #ChatWindow().launch()

