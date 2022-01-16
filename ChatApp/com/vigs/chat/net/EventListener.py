class EventSource:
    def __init__(self, sourceId):
        self.sourceId = sourceId

    def getSourceId(self):
        return self.sourceId

class EventTarget:
    def __init__(self, targetId):
        self.targetId = targetId

    def getTargetId(self):
        return self.targetId

class EventListener:

    def onData(self, msgData, eventSource: EventSource):
        # do nothing, child classes to provide implementation
        pass
