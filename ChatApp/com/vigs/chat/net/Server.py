import socket
import threading
import traceback
import select
import time

import com.vigs.chat.message.Messages as Messages
from com.vigs.chat.net.EventListener import EventTarget
from com.vigs.chat.net.EventListener import EventSource
from com.vigs.chat.net.EventListener import EventListener


class Server:

    def __init__(self, eventListener: EventListener):
        self.eventListener = eventListener
        self.clientSockets = {}
        self.clientSocketsToConnIdDict = {}
        self.start()
        self.connectionIdGenerator = 0

    def start(self):
        self.socket = socket.create_server(address=(socket.gethostname(), 60000))

        'Start a thread to purge closed connections'
        #threadPurgeInactiveConns = threading.Thread(target=self.purgeInActiveConnections, name="Thread-PurgeInactiveConns")
        #threadPurgeInactiveConns.start()


        'Start a thread to read incoming messages from client connections'
        threadReadMessages = threading.Thread(target=self.readIncomingMessages, name="Thread-ReadIncomingMessages")
        threadReadMessages.start()

        'Start a thread to accept incoming client connections'
        threadAcceptConnections = threading.Thread(target=self.acceptConnections, name="Thread-AcceptConnections")
        threadAcceptConnections.start()

        print("Server Started")

    def acceptConnections(self):
        while True:
            try:
                clientSocket = self.socket.accept()[0]
                self.connectionIdGenerator += 1
                connId = str(self.connectionIdGenerator)
                self.clientSockets[connId] = clientSocket
                self.clientSocketsToConnIdDict[clientSocket] = connId
            except Exception as ex:
                traceback.print_exception(ex)
                print("Exiting from here")
                exit()

    def send(self, msgData: str, eventTarget: EventTarget):
        targetSocket: socket.socket = self.clientSockets[eventTarget.targetId]
        targetSocket.sendall(bytearray(msgData, "UTF-8"))
        print("Sent response:", msgData, ", to connection: ", targetSocket, ", targetId:", eventTarget.targetId)


    def readIncomingMessages(self):
        while True:
            if len(self.clientSockets) > 0:
                #print("Waiting to read messages")
                dataReadySockets = select.select(self.clientSockets.values(), [], [], 1.0)[0]
                if len(dataReadySockets) >0:
                    print("Messages available to read")

                for clientSocket in dataReadySockets:
                    clientSocketRef: socket.socket = clientSocket ## just and just to specify datatype, so that class methods can be seen at coding time
                    try:
                            data = clientSocketRef.recv(99999)
                            if len(data) > 0:
                                msgData = data.decode()
                                print("Message received from: ", clientSocketRef.getpeername(), ", Message: ", msgData)
                                self.eventListener.onData(msgData, EventSource(sourceId=self.clientSocketsToConnIdDict[clientSocketRef]))

                            else:
                                print("NULL DATA RECEIVED FROM SOCKET, WHY????", clientSocketRef)
                    except Exception as ex:
                        traceback.print_exception(ex)
                        #print("Closing socket and exiting app")
                        #self.socket.close()
                        #exit()
            ##print("Going to sleep, will wake up later")
            time.sleep(1)

    def purgeInActiveConnections(self):
        while True:
            # check whether the client connection is still alive or not
            if len(self.clientSockets) >0:
                clientSocket:socket.socket = None
                for clientSocket in self.clientSockets:
                    try:
                        #networkForm = self.messageLexer.write(Messages.HBMessage(fromUser="Server", sentTime=time.gmtime()))
                        clientSocket.sendall(bytearray("TestMessage", "UTF-8"))
                    except Exception as ex:
                        traceback.print_exception(ex)
                        print("Exception occurred on connection:", clientSocket, ", purging it")
                        self.clientSockets.remove(clientSocket)
                        print("Removed Connection:", clientSocket)
            time.sleep(1)

    def justPrintSomething(self):
        print("Just Printing Something")


#Server.justPrintSomething()
