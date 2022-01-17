from com.vigs.chat.data.User import User
from com.vigs.chat.data.LoginStatus import LoginStatus
from com.vigs.chat.net.EventListener import EventListener
from com.vigs.chat.net.EventListener import EventSource
from com.vigs.chat.message.Lexer import MessageLexer
from com.vigs.chat.net.Client import Client
import com.vigs.chat.message.Messages as Messages
import time

from abc import ABC, abstractmethod


class ChatClient(EventListener, ABC):

    def __init__(self):
        print("ChatClient Constructor called")
        self.messageLexer = MessageLexer()
        self.clientSocket = Client(self)


    def onData(self, msgData, eventSource: EventSource):
        # do nothing, child classes to provide implementation
        message: Messages.Message = self.messageLexer.read(msgData)
        print("Message Received:", message)
        if isinstance(message, Messages.LoginStatusMessage):
            self.processLoginResponse(loginStatusMessage=message)


    def loginUser(self, login:str, password:str):
        self.loggedInUser = login
        self.sendToServer(Messages.LoginMessage(fromUser=login, password=password, sentTime=time.time()))


    def processLoginResponse(self, loginStatusMessage: Messages.LoginStatusMessage):
        match loginStatusMessage.loginStatus:
            case LoginStatus.ON:
                self.onLoginSuccess()
            case LoginStatus.OFF:
                self.onLoginSuccess()
            case LoginStatus.FAILURE:
                self.onLoginFailure(error=loginStatusMessage.error)


    def sendChatMessage(self, fromUser: str, toUser: str, message: str):
        chatMessage = Messages.ChatMessage(fromUser=fromUser, toUser=toUser, messageText=message, sentTime=time.ctime())
        self.sendToServer(chatMessage)

    def sendToServer(self, message: Messages.Message):
        networkMessage:str = self.messageLexer.write(message)
        self.clientSocket.send(message=networkMessage)


    @abstractmethod
    def onLoginSuccess(self):
        pass

    @abstractmethod
    def onLogoffSuccess(self):
        pass

    @abstractmethod
    def onLoginFailure(self, error):
        pass



