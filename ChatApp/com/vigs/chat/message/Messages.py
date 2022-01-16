from com.vigs.chat.Constants import Constants
from com.vigs.chat.data.User import User
from com.vigs.chat.data.LoginStatus import LoginStatus

class Message:
    pass


class LoginMessage(Message):

    def __init__(self, fromUser:str, password:str, sentTime:str):
        self.fromUser = fromUser
        self.password = password
        self.sentTime = sentTime

    def __str__(self):
        toStr = "LoginMessage[fromUser: " + self.fromUser \
                + ", sentTime: " + self.sentTime \
                + "]"
        return toStr

    def msgType(self):
        return Constants.MESSAGE_TYPE_LOGIN


class LogoffMessage(Message):

    def __init__(self, fromUser, sentTime):
        self.fromUser = fromUser
        self.sentTime = sentTime

    def __str__(self):
        toStr = "LogoffMessage[fromUser: " + self.fromUser \
                + ", sentTime: " + self.sentTime \
                + "]"

    def msgType(self):
        return Constants.MESSAGE_TYPE_LOGOFF


class LoginStatusMessage(Message):
    def __init__(self, user: User, loginStatus: LoginStatus, error: str, chatRooms):
        self.user = user
        self.loginStatus = loginStatus
        self.error = error
        self.chatRooms = chatRooms

    def __str__(self):
        toStr = "LoginStatusMessage[user: " + str(self.user) \
                + ", loginStatus: " + str(self.loginStatus) \
                + ", chatRooms: " + str(self.chatRooms) \
                + "]"
        return toStr

    def msgType(self):
        return Constants.MESSAGE_TYPE_LOGINSTATUS


class ChatMessage(Message):

    def __init__(self, fromUser, toUser, messageText, sentTime):
        self.fromUser = fromUser
        self.toUser = toUser
        self.messageText = messageText
        self.sentTime = sentTime

    def __str__(self):
        toStr = "ChatMessage[fromUser: " + self.fromUser \
                + ", toUser:" + self.toUser \
                + ", messageText: " + self.messageText \
                + ", sentTime: " + self.sentTime \
                + "]"
        return toStr

    def msgType(self):
        return Constants.MESSAGE_TYPE_CHAT


class HBMessage(Message):
    def __init__(self, fromUser, sentTime):
        self.fromUser = fromUser
        self.sentTime = sentTime

    def __str__(self):
        toStr = "HBMessage[fromUser: " + self.fromUser \
                + ", sentTime: " + self.sentTime \
                + "]"
        return toStr

    def msgType(self):
        return Constants.MESSAGE_TYPE_HB
