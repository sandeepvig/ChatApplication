from com.vigs.chat.net.EventListener import EventSource

class LoginSession:

    def __init__(self, login: str, sessionid: str):
        self.login = login
        self.sessionid = sessionid

    def __str__(self):
        return "LoginSession[login: " + self.login + ", sessionid: " + self.sessionid + "]"

