import json
import time
import random

class Utils:
    def getTime():
        CurentTime = time.strftime("%H:%M:%S")
        return CurentTime

    def getRandomID():
        id = []
        id.append(int(''.join([str(random.randint(0, 9)) for _ in range(2)])))
        id.append(int(''.join([str(random.randint(0, 9)) for _ in range(8)])))
        return id

    def isPromoting(currentRole, newRole):
        if newRole == 2:
            return True

        elif newRole == 4:
            if currentRole == 2:
                return False
            else:
                return True

        elif newRole == 3:
            if currentRole == 4:
                return False
            else:
                return True

        elif newRole == 1:
            return False

    def getContentUpdaterInfo():
        return open(f"../../ContentUpdater/lastversion.txt", 'r').read().split('...')

    def getFingerprintData(resourceSha):
        return json.dumps(json.loads(open(f"../../ContentUpdater/Update/{resourceSha}/fingerprint.json", 'r').read()))