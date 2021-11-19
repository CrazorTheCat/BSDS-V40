import time
import random

class Utils:
    def GetTime(self):
        CurentTime = time.strftime("%H:%M:%S")
        return CurentTime

    def GetRoomID(self):
        id = [0, 0]
        id[0] = int(''.join([str(random.randint(0, 9)) for _ in range(1)]))
        id[1] = int(''.join([str(random.randint(0, 9)) for _ in range(8)]))
        return id