from com.vigs.chat.data.User import User
from com.vigs.chat.ui.LoginWindow import LoginWindow
from com.vigs.chat.Application import Application

class ChatClient:

    def __init__(self):
        self.application = Application()

    def launch(self):
        self.loginWindow = LoginWindow(self.application)
        self.loginWindow.launch()


ChatClient().launch()


