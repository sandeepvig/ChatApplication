import threading

from com.vigs.chat.ChatClient import ChatClient
from com.vigs.chat.ui.LoginWindow import LoginWindow
from com.vigs.chat.ui.ChatWindow import ChatWindow

class ChatClientImpl(ChatClient):

    def __init__(self):
        print("ChatClientImpl Constructor calleed")
        (ChatClient).__init__(self)

        loginWindowThread = threading.Thread(target=self.launchLoginWindow, name="Thread-LaunchLoginWindow")
        loginWindowThread.start()

    def onLoginSuccess(self):
        chatWindowThread = threading.Thread(target=self.launchChatWindow, name="Thread-LaunchChatWindow")
        chatWindowThread.start()

    def onLogoffSuccess(self):
        pass

    def onLoginFailure(self, error):
        pass

    def launchLoginWindow(self):
        loginWindow = LoginWindow(chatClient=self)
        loginWindow.launch()

    def launchChatWindow(self):
        chatWindow = ChatWindow(chatClient=self, loginUser=self.loggedInUser)
        chatWindow.launch()

