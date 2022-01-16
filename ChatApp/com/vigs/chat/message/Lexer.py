import datetime
import time

import com.vigs.chat.message.Messages as Messages
from com.vigs.chat.Constants import Constants
from com.vigs.chat.data.LoginStatus import LoginStatus


class MessageLexer:
    def __init__(self):
        pass

    def read(self, message):
        fields = message.split(sep=Constants.FIELDS_SEP)
        attributes = {}
        for field in fields:
            keyValue = field.split(sep=Constants.KEY_VALUE_SEP)
            print("keyValue:", keyValue)
            key = keyValue[0]
            value = keyValue[1]
            attributes[key] = value

        serviceForm = None
        fromUser = attributes[Constants.Fields.FROM_USER]
        sentTime = attributes[Constants.Fields.SENT_TIME]
        match attributes[Constants.MESSAGE_TYPE]:
            case Constants.MESSAGE_TYPE_CHAT:
                toUser = attributes[Constants.Fields.TO_USER]
                serviceForm = Messages.ChatMessage(fromUser=fromUser, toUser=toUser, sentTime=sentTime)
            case Constants.MESSAGE_TYPE_HB:
                serviceForm = Messages.HBMessage(fromUser=fromUser, sentTime=sentTime)
            case Constants.MESSAGE_TYPE_LOGIN:
                serviceForm = Messages.LoginMessage(fromUser=fromUser, password=attributes[Constants.Fields.PASSWORD], sentTime=sentTime)
            case Constants.MESSAGE_TYPE_LOGOFF:
                serviceForm = Messages.LogoffMessage(fromUser=fromUser, sentTime=sentTime)

        return serviceForm

    def write(self, message):
        sentTime = time.strftime("%Y-%m-%d %H:%M:%S")  # VIGS_RELEARN Datetime formatting
        strMessage = "MsgType=" + message.msgType() \
                     + Constants.FIELDS_SEP \
                     + Constants.Fields.SENT_TIME + Constants.KEY_VALUE_SEP + sentTime

        if isinstance(message, Messages.LoginStatusMessage):
            strMessage += Constants.FIELDS_SEP + Constants.Fields.LOGIN_STATUS + Constants.KEY_VALUE_SEP + message.loginStatus.name
            if message.loginStatus == LoginStatus.FAILURE:
                strMessage += Constants.FIELDS_SEP + Constants.Fields.ERROR_MSG + Constants.KEY_VALUE_SEP + message.error
        else:
            strMessage += Constants.FIELDS_SEP + Constants.Fields.FROM_USER + Constants.KEY_VALUE_SEP + message.fromUser

            if isinstance(message, Messages.LoginMessage):
                strMessage += Constants.FIELDS_SEP \
                                + Constants.Fields.PASSWORD + Constants.KEY_VALUE_SEP + message.password
            elif isinstance(message, Messages.ChatMessage):
                strMessage += Constants.FIELDS_SEP \
                              + Constants.Fields.TO_USER + message.toUser \
                              + Constants.FIELDS_SEP \
                              + Constants.Fields.MESSAGE_TEXT + Constants.KEY_VALUE_SEP + message.messageText

        return strMessage




