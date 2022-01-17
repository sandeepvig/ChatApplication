import select
import socket
import threading
import time
import traceback

from com.vigs.chat.net.EventListener import EventSource
from com.vigs.chat.net.EventListener import EventTarget
from com.vigs.chat.net.EventListener import EventListener
import com.vigs.chat.message.Messages as Messages


class Client:

    def __init__(self, eventListener: EventListener):
        self.eventListener = eventListener
        self.start()


    def start(self):
        self.clientSocket = socket.create_connection(address=(socket.gethostname(), 60000))

        'Start a heartbeat sender thread'
        #hbSenderThread = threading.Thread(target=self.sendHB, name="HBSenderThread")
        #hbSenderThread.start()

        messageReaderThread = threading.Thread(target=self.readIncomingMessages, name="Thread-IncomingMessageReader")
        messageReaderThread.start()


    def stop(self):
        print("Closing Socket Connection")
        self.clientSocket.close()
        print("Socket Connection Closed")

    def send(self, message: str):
        ## VIGS_RELEARN use sendall() instead of send()
        self.clientSocket.sendall(bytearray(message, "UTF-8"))
        print("Sent Message: ", message)


    def sendHB(self):
        messageSeq = 0
        while True:
            messageSeq += 1
            messageToSend = self.messageLexer.write(Messages.HBMessage(fromUser="vigs", sentTime=time.gmtime())) + "|Sequence=" + str(messageSeq)
            self.clientSocket.sendall(bytearray(messageToSend, "UTF-8"))
            print("Sent Message:", messageToSend)
            time.sleep(1000)


    def readIncomingMessages(self):
        counter = 0
        while True:
            try:
                print("Counter: ", counter)
                data = self.clientSocket.recv(9999)
                print("Message received: ", str(data.decode()))
                self.eventListener.onData(msgData=str(data.decode()), eventSource=EventSource("server"))
            except Exception as ex:
                traceback.print_exception(ex)
                print("Exception occured in readIncomingMessages:", ex)

            counter += 1
