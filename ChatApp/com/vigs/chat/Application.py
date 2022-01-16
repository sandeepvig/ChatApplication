import com.vigs.chat.message.Messages as Messages
from com.vigs.chat.net.Client import Client
import time

class Application:
    def __init__(self):
        self.clientSocket = Client(self)

    def loginUser(self, login:str, password:str):
        self.clientSocket.send(Messages.LoginMessage(fromUser=login, password=password, sentTime=time.time()))

    def onLoginResponse(self):
        pass


