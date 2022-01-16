from com.vigs.chat.data.User import User
from com.vigs.chat.data.LoginStatus import LoginStatus
from com.vigs.chat.net.EventListener import EventListener
from com.vigs.chat.net.EventListener import EventSource
from com.vigs.chat.message.Lexer import MessageLexer
from com.vigs.chat.net.Client import Client
import com.vigs.chat.message.Messages as Messages
import time

from com.vigs.chat.ui.ChatWindow import ChatWindow


class ChatClient(EventListener):

    def __init__(self):
        self.messageLexer = MessageLexer()
        self.clientSocket = Client(self)

    def onData(self, msgData, eventSource: EventSource):
        # do nothing, child classes to provide implementation
        message: Messages.Message = self.messageLexer.read(msgData)
        print("Message Received:", message)
        if isinstance(message, Messages.LoginStatusMessage):
            if message.loginStatus == LoginStatus.ON:
                print("Launching ChatWindow")
                ChatWindow().launch()

    def loginUser(self, login:str, password:str):
        networkMessage = self.messageLexer.write(Messages.LoginMessage(fromUser=login, password=password, sentTime=time.time()))
        self.clientSocket.send(networkMessage)

    def onLoginResponse(self):
        pass



