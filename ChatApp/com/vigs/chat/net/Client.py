import socket
import threading
import time

import com.vigs.chat.Application as Application
import com.vigs.chat.message.Messages as Messages
from com.vigs.chat.message.Lexer import MessageLexer

class Client:

    def __init__(self, application:Application):
        self.application = application
        self.messageLexer = MessageLexer()
        self.start()

    def start(self):
        self.clientSocket = socket.create_connection(address=(socket.gethostname(), 60000))

        'Start a heartbeat sender thread'
        #hbSenderThread = threading.Thread(target=self.sendHB, name="HBSenderThread")
        #hbSenderThread.start()

    def stop(self):
        print("Closing Socket Connection")
        self.clientSocket.close()
        print("Socket Connection Closed")

    def send(self, message:Messages.Message):
        networkForm:str = self.messageLexer.write(message)
        ## VIGS_RELEARN use sendall() instead of send()
        self.clientSocket.sendall(bytearray(networkForm, "UTF-8"))
        print("Sent Message: ", networkForm)

    def sendHB(self):
        messageSeq = 0
        while True:
            messageSeq += 1
            messageToSend = self.messageLexer.write(Messages.HBMessage(fromUser="vigs", sentTime=time.gmtime())) + "|Sequence=" + str(messageSeq)
            self.clientSocket.sendall(bytearray(messageToSend, "UTF-8"))
            print("Sent Message:", messageToSend)
            time.sleep(1000)

