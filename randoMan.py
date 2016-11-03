## picks a random move ##

import bot
import random

class RandoMan(bot.Bot):
    'Random bot.'

    def getMove(self, boardArr):
        possibleMoves = []
        for i,row in enumerate(boardArr):
            for j,entry in enumerate(row):
                if entry[0]==0:
                    possibleMoves.append((i,j,0))
                if entry[1]==0:
                    possibleMoves.append((i,j,1))
        if len(possibleMoves)==0:
            return (-1,-1,-1)
        else:
            r = random.randint(0,len(possibleMoves)-1)
            return possibleMoves[r]
