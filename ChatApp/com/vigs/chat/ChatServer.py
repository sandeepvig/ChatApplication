import com.vigs.chat.message.Messages as Messages
from com.vigs.chat.message.Lexer import MessageLexer
from com.vigs.chat.net.Server import Server
from com.vigs.chat.net.EventListener import EventSource
from com.vigs.chat.net.EventListener import EventTarget
from com.vigs.chat.net.EventListener import EventListener
from com.vigs.chat.db.UserDAO import UserDAO
from com.vigs.chat.data.User import User
from com.vigs.chat.data.LoginStatus import LoginStatus
from com.vigs.chat.data.LoginSession import LoginSession
import traceback
import time
import socket


class ChatServer(EventListener):

    def __init__(self):
        self.messageLexer = MessageLexer()
        self.server = Server(self)
        self.userDAO = UserDAO()
        self.loginSessions = {"dummysessionid": None}

        self.userDAO.getAllUsers()

    def onData(self, msgData, eventSource: EventSource):
        response: Messages.Message = self.processMessage(msgData=msgData, eventSource=eventSource)
        if response is not None:
            self.server.send(self.messageLexer.write(response), EventTarget(targetId=eventSource.getSourceId()))

    def processMessage(self, msgData: str, eventSource: EventSource):
        message = self.messageLexer.read(message=msgData)
        print("Message Received:", message)
        if type(message) == Messages.LoginMessage:
            return self.loginUser(loginMessage=message, eventSource=eventSource)
        elif type(message) == Messages.LogoffMessage:
            pass
        elif type(message) == Messages.ChatMessage:
            return self.deliverChatMessage(chatMessage=message)


    def loginUser(self, loginMessage: Messages.LoginMessage, eventSource: EventSource):
        try:
            user: User = self.userDAO.getUser(loginMessage.fromUser)
            if user is not None and user.password == loginMessage.password:
                loginSession = LoginSession(login=user.login, sessionid=eventSource.getSourceId())
                self.loginSessions[user.login] = loginSession
                print("LoginSession created:", loginSession)
                return Messages.LoginStatusMessage(user=user, loginStatus=LoginStatus.ON, error=None, chatRooms=None)
            else:
                return Messages.LoginStatusMessage(user=None, loginStatus=LoginStatus.FAILURE, error="Invalid username/password", chatRooms=None)
        except Exception as ex:
            traceback.print_exception(ex)
            return Messages.LoginStatusMessage(user=None, loginStatus=LoginStatus.FAILURE, error="Error while login, try again", chatRooms=None)

    def deliverChatMessage(self, chatMessage: Messages.ChatMessage):
        toUser = chatMessage.toUser
        toUserLoginSession: LoginSession = self.loginSessions[toUser]
        print("toUser:", toUser, "toUserLoginSession:", toUserLoginSession)

        if LoginSession is not None:
            eventTargetId = toUserLoginSession.sessionid
            self.server.send(self.messageLexer.write(message=chatMessage), eventTarget=EventTarget(targetId=eventTargetId))
            print("Delivered:", chatMessage, )


    def purgeInActiveSessions(self):
        while True:
            # check whether the client connection is still alive or not
            if len(self.clientSockets) > 0:
                clientSocket: socket.socket = None
                for clientSocket in self.clientSockets:
                    try:
                        networkForm = self.messageLexer.write(
                            Messages.HBMessage(fromUser="Server", sentTime=time.gmtime()))
                        clientSocket.sendall(bytearray(networkForm, "UTF-8"))
                    except Exception as ex:
                        traceback.print_exception(ex)
                        print("Exception occurred on connection:", clientSocket, ", purging it")
                        self.clientSockets.remove(clientSocket)
                        print("Removed Connection:", clientSocket)
            time.sleep(1)


