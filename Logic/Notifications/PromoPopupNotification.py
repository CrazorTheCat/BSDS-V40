from Logic.Helpers.ChronosFileEntry import ChronosFileEntry
from Logic.Helpers.ChronosTextEntry import ChronosTextEntry
from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class PromoPopupNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        ChronosTextEntry.encode(self)
        ChronosTextEntry.encode(self)
        ChronosTextEntry.encode(self)
        ChronosFileEntry.encode(self)
        self.writeString("Damn how much strings is there here")
        self.writeVint(0)


    def encode(self: Writer, info):
        BaseNotification.encode(self, info)
        ChronosTextEntry.encode(self)
        ChronosTextEntry.encode(self)
        ChronosTextEntry.encode(self)
        ChronosFileEntry.encode(self)
        self.writeString("Damn how much strings is there here")
        self.writeVint(0)

        self.writeInt(0)
        self.writeString('BRAWL TALK IS HERE!')

        self.writeInt(0)
        self.writeString('Legendary Sidekick, MAKE Skin, and MORE!')

        self.writeInt(0)
        self.writeString('Here we go!')

        self.writeString('/36042168-49af-4e79-b5f3-13c8c279bc5c_brawltalkpopup.png')
        self.writeString('28d8d5533ddecebf766daac49f3290415a36fa42')

        self.writeString('brawlstars://extlink?page=https%3A%2F%2Fyoutu.be%2F9jycpItX9l4')
        self.writeVint(3473)
