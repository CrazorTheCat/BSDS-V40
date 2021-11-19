from Logic.Settings.Configuration import Configuration


class PrintManager:
    def printDisabledPrint(self):
        if Configuration.Print["DisabledPrint"] == True:
            print()
            for i,v in Configuration.Print.items():
                if v == False:
                    print(f'{i} printing is disabled in configuration.')
            print()

    def printLogin(self):
        if Configuration.Print["Login"] == True:
            print(f'\nHighID: {self.player.HighID}, LowID: {self.player.LowID}, Token: {self.player.Token}\n')

            print(f'Major: {self.Major}, Minor: {self.Minor}, Build: {self.Build}\n')

            print(f'Fingerprint: {self.FingerprintSha}\n')

            print(f'Device model: {self.DeviceModel}, Android bool: {self.IsAndroid}, Device language: {self.DeviceLanguage}, OS version: {self.OSVersion}\n')

            print(f'OpenUDID: {self.OpenUDID}\n')

            print(f'App version: {self.AppVersion}\n')


    def printAnalytics(self):
        if Configuration.Print["Analytics"] == True:
            print(f'Event: {self.EventType} Info: {self.Event}\n')