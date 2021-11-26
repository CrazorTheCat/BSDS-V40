from Messaging.LogicCommandManager import commandIdentifiers

from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class EndClientTurnMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.client = client
        self.player = player
        self.commmandID = []

    def decode(self):
        self.readBoolean()
        self.readVint()
        self.readVint()
        count = self.readVint()
        for command in range(count):
            self.commmandID.append(self.readVint())
            self.tick1 = self.readVint()
            self.tick2 = self.readVint()
            self.readLogicLong()
            if self.commmandID[command] in commandIdentifiers:
                if type(commandIdentifiers[self.commmandID[command]]) != str:
                    command = commandIdentifiers[self.commmandID[command]]
                    command.decode(self)
                    command.process(self)
            ## Rest is the data

    def process(self):
        if len(self.commmandID) != 0:
            for i in self.commmandID:
                if i in commandIdentifiers:
                    if type(commandIdentifiers[i]) != str:
                        print(f'Received command: {i}: {commandIdentifiers[i].__name__}')
                    else:
                        print(f'Received command: {i}: {commandIdentifiers[i]}')
                else:
                    print(f'Received unknown command with id: {i}.')