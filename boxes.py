#### Foggy boxes AI contest ####

import sys
import time

ASCII_BOX_HEIGHT = 4
ASCII_BOX_WIDTH = 8

class Game:
    'Game class. Runs and displays a game between two bots.'
    
    def __init__(self, player1, player2, boardSize=5):
        self.player1 = player1
        self.player2 = player2
        self.boardSize = boardSize
        self.turnOver = False
        self.moveCount = 0
        ##board array stored as array of triples. The triples represent points.
        ##(x,y,z) where x represents eastern wall, y southern, z square control
        ##x or y==0 indicates no wall
        ##x or y==1 player 1 built wall
        ##x or y==2 player 2 built wall
        ##similar for z
        ##eastern boundary points cannot have eastern wall
        ##southern boundary points cannot have southern wall
        ##the southeast corner is always (-1,-1,-1)
        self.boardArr = [[[0,0,0] for i in range(self.boardSize)] for j in range(self.boardSize)]
        for i in range(self.boardSize):
            self.boardArr[self.boardSize-1][i] = [0,-1,-1]
            self.boardArr[i][self.boardSize-1] = [-1,0,-1]
        self.boardArr[self.boardSize-1][self.boardSize-1] = [-1,-1,-1]

    def displayBoard(self):
        #ascii art mofo
        sys.stdout.write("#"*(self.boardSize*ASCII_BOX_WIDTH)+"\n\n")
        for i in range(self.boardSize*ASCII_BOX_HEIGHT-2):
            for j in range(self.boardSize):

                ##grab box data as triple
                box_data = self.boardArr[i/ASCII_BOX_HEIGHT][j]
                if i%ASCII_BOX_HEIGHT==0:
                    ##line with dots
                    if box_data[0]>0:
                        ##east edge exists
                        sys.stdout.write("."+"-"*ASCII_BOX_WIDTH)
                    else:
                        ##east edge empty
                        sys.stdout.write("."+" "*ASCII_BOX_WIDTH)
                else:
                    ##default fill
                    fill = " "
                    if box_data[2]>0:
                        if box_data[2]==1:
                            fill = "#"
                        else:
                            fill = "`"

                    ##line without dots
                    if box_data[1]>0:
                        ##south edge exists
                        sys.stdout.write("|"+fill*ASCII_BOX_WIDTH)
                    else:
                        ##south edge empty
                        sys.stdout.write(" "+fill*ASCII_BOX_WIDTH)

            sys.stdout.write("\n")
        sys.stdout.write("#"*(self.boardSize*ASCII_BOX_WIDTH)+"\n")
        sys.stdout.write("\n")

    def updateBoard(self, move, player):
        #updates the board with new move
        row = move[0]
        col = move[1]
        wall = move[2]
        self.boardArr[row][col][wall] = player

        self.turnOver = True
        if self.checkBoxFull(row, col) and self.boardArr[row][col][2]==0:
            self.boardArr[row][col][2] = player
            self.turnOver = False
        if self.checkBoxFull(row-1, col) and self.boardArr[row-1][col][2]==0:
            self.boardArr[row-1][col][2] = player
            self.turnOver = False
        if self.checkBoxFull(row, col-1) and self.boardArr[row][col-1][2]==0:
            self.boardArr[row][col-1][2] = player
            self.turnOver = False


    def checkBoxFull(self, row, col):
        #check if box has all four edges
        if row >= self.boardSize-1 or col >= self.boardSize-1 or row < 0 or col < 0:
            return False
        elif self.boardArr[row][col][0]>0 and self.boardArr[row][col][1]>0 and self.boardArr[row+1][col][0]>0 and self.boardArr[row][col+1][1]>0:
            return True
        else:
            return False

    def displayBoardArray(self):
        #print self.boardArray nicely for debugging
        for i in range(self.boardSize):
            print self.boardArr[i]

    def takeTurn(self, player):
        #take turn, input player
        self.turnOver = False
        while not self.turnOver and self.moveCount < self.boardSize*(self.boardSize-1)*2:
            if player==1:
                move = self.player1.getMove(self.boardArr)
            if player==2:
                move = self.player2.getMove(self.boardArr)
            self.updateBoard(move,player)
            self.displayBoard()
            self.moveCount += 1
            time.sleep(.1)

    def run(self):
        gameOver = False
        while self.moveCount < self.boardSize*(self.boardSize-1)*2:
            self.takeTurn(1)
            self.takeTurn(2)
        
        #check who won
        player1Total = 0
        player2Total = 0
        for row in self.boardArr:
            for entry in row:
                if entry[2]==1:
                    player1Total += 1
                if entry[2]==2:
                    player2Total += 1

        print player1Total
        print player2Total
        
        if player1Total > player2Total:
            print "Player 1 wins"
        elif player2Total > player1Total:
            print "Player 2 wins"
        else:
            print "TIE"

import testBot as t
import randoMan as r
g = Game(r.RandoMan(),r.RandoMan(),10)
g.run()

