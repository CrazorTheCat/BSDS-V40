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
        # ChronosTextEntry.encode(self)
        # ChronosTextEntry.encode(self)
        # ChronosTextEntry.encode(self)
        # ChronosFileEntry.encode(self)

        self.writeInt(0)
        self.writeString(info[1]['Title'])

        self.writeInt(0)
        self.writeString(info[1]['Subtitle'])

        self.writeInt(0)
        self.writeString(info[1]['ButtonText'])

        self.writeString(info[1]['ImageUrl'])
        self.writeString('28d8d5533ddecebf766daac49f3290415a36fa42')

        self.writeString(info[1]['RedirectLink'])
        self.writeVint(3473)
