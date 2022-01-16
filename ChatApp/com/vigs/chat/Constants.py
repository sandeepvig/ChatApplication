class Constants:
    MESSAGE_TYPE = "MsgType"
    FIELDS_SEP = "|"
    KEY_VALUE_SEP = "="

    MESSAGE_TYPE_CHAT = "Chat"
    MESSAGE_TYPE_HB = "Heartbeat"
    MESSAGE_TYPE_LOGIN = "Login"
    MESSAGE_TYPE_LOGOFF = "Logoff"
    MESSAGE_TYPE_LOGINSTATUS = "LoginStatus"

    class Fields:
        FROM_USER = "FromUser"
        TO_USER = "ToUser"
        MESSAGE_TEXT = "Text"
        SENT_TIME = "SentTime"
        RECEIVED_TIME = "ReceivedTime"
        PASSWORD = "Password"
        LOGIN_STATUS = "LoginStatus"
        ERROR_MSG = "ErrorMsg"

