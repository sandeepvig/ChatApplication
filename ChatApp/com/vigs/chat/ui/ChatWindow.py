import tkinter
import threading

from com.vigs.chat.ChatClient import ChatClient
from com.vigs.chat.data.User import User
from com.vigs.chat.ui.UserDisplayName import UserDisplayName

class ChatWindow:
    def __init__(self, chatClient: ChatClient, loginUser: str):
        self.loginUser = loginUser
        self.chatClient = chatClient
        self.build()

    def launch(self):
        self.root.mainloop()

    def build(self):
        self.root = tkinter.Tk()
        self.root.title(str(self.loginUser))
        self.buildChatRoomList()
        self.buildChatRoomLabel()
        self.buildChatHistory()
        self.buildChatMessageInput()
        self.loadChatRooms()

        self.registerEventHandlers()

    def buildChatRoomList(self):
        self.chatRoomList = tkinter.Listbox(self.root)
        self.chatRoomList.grid(row=0, column=0, rowspan=3, sticky=tkinter.NSEW)

    def buildChatRoomLabel(self):
        self.chatRoomLabel = tkinter.Label(self.root, text="Room-XXX")
        self.chatRoomLabel.grid(row=0, column=1, sticky=tkinter.NSEW)

    def buildChatHistory(self):
        self.txtChatHistory = tkinter.Text(self.root)
        self.txtChatHistory.grid(row=1, column=1, sticky=tkinter.NSEW)

    def buildChatMessageInput(self):
        self.txtChatMessage = tkinter.Entry(self.root)
        self.txtChatMessage.grid(row=2, column=1, sticky=tkinter.NSEW)

    def loadChatRooms(self):
        #self.userList.insert(User(login="atiwari", fname="Abhishek", lname="Tiwari"),"Abhishek Tiwari")
        #self.userList.insert(User(login="vvirmani", fname="Vineet", lname="Vineet"), "Vineet Virmani")
        self.chatRoomList.insert(tkinter.END, UserDisplayName(login="atiwari", fname="Abhishek", lname="Tiwari"))
        self.chatRoomList.insert(tkinter.END, UserDisplayName(login="vvirmani", fname="Vineet", lname="Virmani"))
        self.chatRoomList.insert(tkinter.END, UserDisplayName(login="svig", fname="Sandeep", lname="Vig"))
        self.chatRoomList.insert(tkinter.END, UserDisplayName(login="agupta", fname="Amit", lname="Gupta"))

    def registerEventHandlers(self):
        self.chatRoomList.bind("<<ListboxSelect>>", self.chatRoomSelectionHandler)
        self.txtChatMessage.bind("<Return>", self.sendChatMessage)

    def chatRoomSelectionHandler(self, event):
        self.chatRoomLabel.config(text=self.chatRoomList.get(self.chatRoomList.curselection()[0]))

    def sendChatMessage(self, event):
        toUserDisplayName: str = self.chatRoomList.get(self.chatRoomList.curselection()[0])
        toUser = toUserDisplayName[toUserDisplayName.rfind("(")+1:len(toUserDisplayName)-1]
        print("toUser:", toUser)
        self.chatClient.sendChatMessage(fromUser=self.chatClient.loggedInUser, toUser=toUser, message=self.txtChatMessage.get())

