import csv


class Cards:

    def getStarpowersID():
        CardSkillsID = []
        with open('Logic/Files/assets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[7] == '4' and row[4].lower() != "true" and row[5].lower() != "true":
                        # print(line_count - 2, row[7], row[3], row[4], row[5])
                        CardSkillsID.append(line_count - 2)
                    line_count += 1

            return CardSkillsID

    def get_spg_by_brawlerID(self, brawlerID, type):
        char_file = open('Logic/Files/assets/csv_logic/characters.csv')
        csv_reader = csv.reader(char_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0 or line_count == 1:
                line_count += 1
            else:
                line_count += 1
                if line_count == brawlerID + 3:
                    name = row[0]
                    line_count += 1

                    cards_file = open('Logic/Files/assets/csv_logic/cards.csv')
                    csv_reader = csv.reader(cards_file, delimiter=',')
                    line_count = 0

                    for row in csv_reader:
                        if line_count == 0 or line_count == 1:
                            line_count += 1
                        else:
                            line_count += 1
                            if type == 4:
                                if row[6].lower() == '4' and row[3] == name:
                                    id = line_count - 3
                                    char_file.close()
                                    cards_file.close()
                                    return id

                            elif type == 5:
                                if row[3] == name and row[6].lower() == '5':
                                    id = line_count - 3
                                    char_file.close()
                                    cards_file.close()
                                    return id

    def get_unlocked_spg(self, brawlerID):
        char_file = open('Logic/Files/assets/csv_logic/characters.csv')
        csv_reader = csv.reader(char_file, delimiter=',')
        line_count = 0
        id = []

        for row in csv_reader:
            if line_count == 0 or line_count == 1:
                line_count += 1
            else:
                line_count += 1
                if line_count == brawlerID + 3:
                    name = row[0]
                    line_count += 1

                    cards_file = open('Logic/Files/assets/csv_logic/cards.csv')
                    csv_reader = csv.reader(cards_file, delimiter=',')
                    line_count = 0

                    for row in csv_reader:
                        if line_count == 0 or line_count == 1:
                            line_count += 1
                        else:
                            line_count += 1
                            if row[6].lower() == '4' and row[3] == name and row[4] != "true" or row[3] == name and row[6].lower() == '5' and row[4] != "true":
                                print(row[0], line_count - 3)
                                id.append(line_count - 3)

                    char_file.close()
                    cards_file.close()
                    return id

    def getBrawlersUnlockID():
        CardUnlockID = []
        with open('Logic/Files/assets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[7] == '0' and row[4].lower() != "true" and row[5].lower() != "true":
                        (line_count - 2, row[7], row[3], row[4], row[5])
                        CardUnlockID.append(line_count - 2)
                    line_count += 1

            return CardUnlockID
