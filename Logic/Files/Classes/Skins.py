import csv


class Skins:

    def getSkinsID():

        SkinsID = []

        with open('Logic/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[2].lower() != "true":
                        (line_count - 2)
                        SkinsID.append(line_count - 2)
                    if row[0] != "":
                        line_count += 1

            return SkinsID

    def getBrawlerBySkin(self, skinID):
        with open('Logic/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if line_count - 2 == skinID:
                        confName = row[1]
                        with open('Logic/Files/assets/csv_logic/skin_confs.csv') as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count2 = 0
                            for row2 in csv_reader:

                                if line_count2 == 0 or line_count2 == 1:
                                    line_count2 += 1
                                else:
                                    if row2[0] == confName:
                                        brawlerName = row2[1]
                                        with open('Logic/Files/assets/csv_logic/characters.csv') as csv_file:
                                            csv_reader = csv.reader(csv_file, delimiter=',')
                                            line_count3 = 0
                                            for row3 in csv_reader:
                                                if line_count3 == 0 or line_count3 == 1:
                                                    line_count3 += 1
                                                else:
                                                    if row3[0] == brawlerName:
                                                        return line_count3 - 2
                                                    if row3[0] != "":
                                                        line_count3 += 1
                                    if row2[0] != "":
                                        line_count2 += 1
                    if row[0] != "":
                        line_count += 1

    def getSkinInfoByID(id):
        with open('Logic/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if line_count - 2 == id:
                        formatedRow = []
                        formatedRow.append(line_count - 2)
                        for i in row:
                            if i != '':
                                formatedRow.append(i)
                        print(formatedRow)
                        break
                    line_count += 1

    def getSkinsForBrawler(name):
        name = name + '_'
        with open('Logic/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[2].lower() != "true" and row[20].startswith(name.lower()):
                        formatedRow = []
                        formatedRow.append(line_count - 2)
                        for i in row:
                            if i != '':
                                formatedRow.append(i)
                        print(formatedRow)
                    line_count += 1

    def getSkinInfoByName(name):
        with open('Logic/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[0] == name:
                        formatedRow = []
                        formatedRow.append(line_count - 2)
                        for i in row:
                            if i != '':
                                formatedRow.append(i)
                        print(formatedRow)
                        break
                    line_count += 1

    def getSkinsInfo():
        with open('Logic/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    formatedRow = []
                    formatedRow.append(line_count - 2)
                    for i in row:
                        if i != '':
                            formatedRow.append(i)
                    print(formatedRow)
                    line_count += 1
