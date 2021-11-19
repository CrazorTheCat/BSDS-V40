class GlobalID:
    def getClassID(self, globalId):
        return (globalId / 1000000 + (globalId >> 31)) - (globalId * 1125899907 >> 63)