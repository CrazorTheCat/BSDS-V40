import random
import string

from Logic.Files.Classes.Cards import Cards
from Logic.Files.Classes.Characters import Characters
from Logic.Files.Classes.Locations import Locations
from Logic.Files.Classes.PlayerThumbnails import PlayerThumbnails
from Logic.Files.Classes.Skins import Skins
from Logic.Files.Classes.Pins import Pins
from Logic.Client import DevicesManager


class Players:
    def __init__(self):
        pass

    HighID = 0
    LowID = 0
    Token = ""
    Name = "Guest"
    isRegistred = False
    isBanned = False

    friends = []

    allianceTry = 0

    trophies = 10000
    highestTrophies = 10000
    experience = 999999
    level = 500
    trophy_road_tier = 105
    coins = 9999999
    gems = 9999999
    tokens = 9999999
    StarTokens = 9999999
    StarPoints = 9999999
    ClubCoins = 9999999
    GearsScrap = 9999999

    thumbnail = 0
    nameColor = 0
    region = "CA"

    brawlerID = 0
    skinID = 0
    starpowerID = 76
    selectedSkin = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0, 46: 0, 47: 0, 49: 0, 50: 0, 51: 0, 52: 0, 53: 0}
    selectedRandomSkin = []
    brawlerState = {0: 2, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2, 11: 2, 12: 2, 13: 2, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 2, 20: 2, 21: 2, 22: 2, 23: 2, 24: 2, 25: 2, 26: 2, 27: 2, 28: 2, 29: 2, 30: 2, 31: 2, 32: 2, 34: 2, 35: 2, 36: 2, 37: 2, 38: 2, 39: 2, 40: 2, 41: 2, 42: 2, 43: 2, 44: 2, 45: 2, 46: 2, 47: 2, 49: 2, 50: 2, 51: 2, 52: 2, 53: 2}
    brawlersTrophies = {0: 1250, 1: 1250, 2: 1250, 3: 1250, 4: 1250, 5: 1250, 6: 1250, 7: 1250, 8: 1250, 9: 1250, 10: 1250, 11: 1250, 12: 1250, 13: 1250, 14: 1250, 15: 1250, 16: 1250, 17: 1250, 18: 1250, 19: 1250, 20: 1250, 21: 1250, 22: 1250, 23: 1250, 24: 1250, 25: 1250, 26: 1250, 27: 1250, 28: 1250, 29: 1250, 30: 1250, 31: 1250, 32: 1250, 34: 1250, 35: 1250, 36: 1250, 37: 1250, 38: 1250, 39: 1250, 40: 1250, 41: 1250, 42: 1250, 43: 1250, 44: 1250, 45: 1250, 46: 1250, 47: 1250, 49: 1250, 50: 1250, 51: 1250, 52: 1250, 53: 1250}
    allSkins = Skins.getSkinsID()
    allMaps = [5, 7, 24]
    allBrawlers = Characters.getBrawlersID()
    allBrawlersUnlock = Cards.getBrawlersUnlockID()
    allStarpowers = Cards.getStarpowersID()
    allPins = Pins.getPinsID()
    allThumbnailsReward = PlayerThumbnails.getThumbnailsID()

    allianceID = [0, 0]

    room_id = [0, 0]
    roomInfo = {
        "eventSlot": 0,
        "mapID": 0,
        "roomType": 0
    }

    clubMailInbox = [

    ]

    doNotDisturb = False
    playerState = False
    lastOnline = 0

    device = DevicesManager.Device

    def CreateAccount(self, highid, lowid, token, overide=False):

        if overide == False:
            self.HighID = int(''.join([str(random.randint(0, 9)) for _ in range(1)]))
            self.LowID = int(''.join([str(random.randint(0, 9)) for _ in range(8)]))
            self.Token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40))
        else:
            self.HighID = highid
            self.LowID = lowid
            self.Token = token

        DBData = {
                'HighID': self.HighID,
                'LowID': self.LowID,
                'Token': self.Token,
                'name': self.Name,
                'allianceID': self.allianceID,
                'PlayerState': self.playerState,
                'LastOnline': self.lastOnline,
                'DoNotDisturb': self.doNotDisturb,
                'brawlerID': self.brawlerID,
                'skinID': self.skinID,
                'selectedSkin': self.selectedSkin,
                'selectedRandomSkin': self.selectedRandomSkin,
                'brawlersTrophies': self.brawlersTrophies,
                'brawlerState': self.brawlerState,
                'starpowerID': self.starpowerID,
                'playericon': self.thumbnail,
                'namecolor': self.nameColor,
                'region': self.region,
                'highestTrophies': self.highestTrophies,
                'IsRegistred': self.isRegistred,
                'trophies': self.trophies,
                'experience': self.experience,
                'level': self.level,
                'gems': self.gems,
                'coins': self.coins,
                'isBanned': self.isBanned,
                'gameroomID': self.room_id,
                'clubMailInbox': self.clubMailInbox,
                "roomInfo": {
                    "eventSlot": 0,
                    "mapID": 0,
                    "roomType": 0
                },
                'friend': self.friends
                }
        return DBData