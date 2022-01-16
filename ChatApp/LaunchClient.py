from com.vigs.chat.ChatClient import ChatClient
from com.vigs.chat.ui.LoginWindow import LoginWindow

chatClient = ChatClient()
loginWindow = LoginWindow(chatClient)
loginWindow.launch()