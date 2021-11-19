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
        print(self.readBoolean())
        print(self.readVint())
        print(self.readVint())
        count = self.readVint()
        print(count)
        for command in range(count):
            self.commmandID.append(self.readVint())
            self.tick1 = self.readVint()
            self.tick2 = self.readVint()
            self.readVLong()
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