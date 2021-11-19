from Logic.Data.DataManager import Reader
from LogicCommand import LogicCommand


class LogicServerCommand:
    def encode(self):
        self.writeVint(0)
        LogicCommand.encode(self)

