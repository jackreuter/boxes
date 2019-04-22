## bot simply scrolls through all options, chooses any option to complete a square
## if no option exists, chooses first option to not give a completion
## otherwise plays first possible option

import bot

class SimpleBot(bot.Bot):

    ## first look for squares to complete
    def getMove(self, boardArr):
        legalMoves = []
        scoringMoves = []
        smartMoves = []

        for i,row in enumerate(boardArr):
            for j,entry in enumerate(row):
                
                ## if east wall is open
                if entry[0]==0:
                    legalMoves.append([i, j, 0])

                    ## if wall completes square
                    if self.completesSquare(boardArr, i, j, 0):
                        scoringMoves.append([i, j, 0])

                    ## if wall does not give opponent completion
                    if not self.givesOpponentSquare(boardArr, i, j, 0):
                        smartMoves.append([i, j, 0])

                ## if south wall is open
                if entry[1]==0:
                    legalMoves.append([i, j, 1])

                    ## if wall completes square
                    if self.completesSquare(boardArr, i, j, 1):
                        scoringMoves.append([i, j, 1])

                    ## if wall does not give opponent completion
                    if not self.givesOpponentSquare(boardArr, i, j, 1):
                        smartMoves.append([i, j, 1])

        ## score if possible
        ## otherwise prevent immediate scoring
        ## otherwise play legal move
        if len(scoringMoves) > 0:
            return scoringMoves[0]

        elif len(smartMoves) > 0:
            return smartMoves[0]

        elif len(legalMoves) > 0:
            return legalMoves[0]

        else:
            return (-1, -1, -1)

    ## checks if a given move will complete a square
    def completesSquare(self, board, row, col, wall):

        ## if east
        if wall==0:

            ## check above
            if self.completesAbove(board, row, col):
                return True

            ## check below
            if self.completesBelow(board, row, col):
                return True

        ## if west
        elif wall==1:
            
            # check left
            if self.completesLeft(board, row, col):
                return True

            # check right
            if self.completesRight(board, row, col):
                return True
        
        ## default
        else:
            return False

    ## check if above three walls exist
    def completesAbove(self, board, row, col):
        if (row==0):
            return False
        else:
            pointNorth = board[row-1][col]
            pointNorthEast = board[row-1][col+1]
            if pointNorth[0] > 0 and pointNorth[1] > 0 and pointNorthEast[1] > 0:
                return True
        return False

    ## check if below three walls exist
    def completesBelow(self, board, row, col):
        if (row==len(board)-1):
            return False
        else:
            pointSouth = board[row+1][col]
            pointEast = board[row][col+1]
            if board[row][col][1] > 0 and pointSouth[0] > 0 and pointEast[1] > 0:
                return True
        return False

    ## check if right three walls exist
    def completesRight(self, board, row, col):        
        if (col==len(board[0])-1):
            return False
        else:
            pointSouth = board[row+1][col]
            pointEast = board[row][col+1]
            if board[row][col][0] > 0 and pointSouth[0] > 0 and pointEast[1] > 0:
                return True
        return False

    ## check if left three walls exist
    def completesLeft(self, board, row, col):
        if (col==0):
            return False
        else:
            pointWest = board[row][col-1]
            pointSouthWest = board[row+1][col-1]
            if pointWest[0] > 0 and pointWest[1] > 0 and pointSouthWest[0] > 0:
                return True
        return False

    ## checks if a given move will give an opponent a square
    def givesOpponentSquare(self, board, row, col, wall):

        ## if east
        if wall==0:

            ## check above
            if self.givesOpponentAbove(board, row, col):
                return True

            ## check below
            if self.givesOpponentBelow(board, row, col):
                return True

        ## if west
        elif wall==1:
            
            # check left
            if self.givesOpponentLeft(board, row, col):
                return True

            # check right
            if self.givesOpponentRight(board, row, col):
                return True
        
        ## default
        else:
            return False

    ## checks if gives square above to opponent
    def givesOpponentAbove(self, board, row, col):
        if (row==0):
            return False
        else:
            pointNorth = board[row-1][col]
            pointNorthEast = board[row-1][col+1]
            if pointNorth[0] > 0 and pointNorth[1] > 0:
                return True
            if pointNorth[0] > 0 and pointNorthEast[1] > 0:
                return True
            if pointNorth[1] > 0 and pointNorthEast[1] > 0:
                return True
        return False

    ## checks if gives square above to opponent
    def givesOpponentBelow(self, board, row, col):
        if (row==len(board)-1):
            return False
        else:
            pointSouth = board[row+1][col]
            pointEast = board[row][col+1]
            if board[row][col][1] > 0 and pointSouth[0] > 0:
                return True
            if board[row][col][1] > 0 and pointEast[1] > 0:
                return True
            if pointSouth[0] > 0 and pointEast[1] > 0:
                return True
        return False

    ## checks if gives square above to opponent
    def givesOpponentLeft(self, board, row, col):
        if (col==0):
            return False
        else:
            pointWest = board[row][col-1]
            pointSouthWest = board[row+1][col-1]
            if pointWest[0] > 0 and pointWest[1] > 0:
                return True
            if pointWest[0] > 0 and pointSouthWest[0] > 0:
                return True
            if pointWest[1] > 0 and pointSouthWest[0] > 0:
                return True
        return False

    ## checks if gives square above to opponent
    def givesOpponentRight(self, board, row, col):
        if (col==len(board[0])-1):
            return False
        else:
            pointSouth = board[row+1][col]
            pointEast = board[row][col+1]
            if board[row][col][0] > 0 and pointSouth[0] > 0:
                return True
            if board[row][col][0] > 0 and pointEast[1] > 0:
                return True
            if pointSouth[0] > 0 and pointEast[1] > 0:
                return True
        return False

