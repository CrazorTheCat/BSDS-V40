from Logic.Entry.ScoreEntry import ScoreEntry
from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class StarPointsNotification:
    ProgressStart = [501, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]
    ProgressEnd = [524, 549, 574, 599, 624, 649, 674, 699, 724, 749, 774, 799, 824, 849, 874, 899, 924, 949, 974, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1499, -64]
    Progress = [500, 524, 549, 574, 599, 624, 649, 674, 699, 724, 749, 774, 799, 824, 849, 874, 885, 900, 920, 940, 960, 980, 1000, 1020, 1040, 1060, 1080, 1100, 1120, 1140, 1150]
    RewardedSP = [20, 50, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250,260, 270, 280, 290, 300, 310, 320, 330, 340, 350]

    def decode(self: Reader):
        BaseNotification.decode(self)
        for i in range(self.readVint()):
            print()
            ScoreEntry.decode(self)

    def encode(self: Writer, info):
        BaseNotification.encode(self, info)
        self.writeVint(len(self.player.brawlersTrophies))
        for id,trophies in self.player.brawlersTrophies.items():
            brawlerInfo = [int(id), trophies]
            if trophies >= 1500:
                brawlerInfo.append(trophies - 1150)
                brawlerInfo.append(350)
            elif trophies >= 501:
                for i in StarPointsNotification.Progress:
                    StarpointsProgressIndex = StarPointsNotification.Progress.index(i)
                    if StarPointsNotification.ProgressStart[StarpointsProgressIndex] <= trophies <= StarPointsNotification.ProgressEnd[StarpointsProgressIndex]:
                        brawlerInfo.append(trophies - i)
                        brawlerInfo.append(StarPointsNotification.RewardedSP[StarpointsProgressIndex])
                        break
            ScoreEntry.encode(self, brawlerInfo)