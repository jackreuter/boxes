## basic ass bot to test the ascii and gameplay and shit ##

import bot

class TestBot(bot.Bot):
    'Basic ass bot.'

    def getMove(self, boardArr):
        for i,row in enumerate(boardArr):
            for j,entry in enumerate(row):
                if entry[0]==0:
                    return (i,j,0)
                if entry[1]==0:
                    return (i,j,1)
        return (-1,-1,-1)
