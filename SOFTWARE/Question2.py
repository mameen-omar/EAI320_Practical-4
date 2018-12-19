import numpy as np
import copy
import queue
import sys


class game:
    #initializer
    def __init__(self, game = None, board = None):
        if(game == None):
            self.board = np.array([["#","#","#"],
                                  ["#","#","#"],
                                  ["#","#","#"]])
            self.againstAI = False
            self.state = "Unfinished"
            self.player1Name = ""
            self.player2Name = ""
            self.playAiCheck()       
            self.setNames()
            self.turn = copy.deepcopy(self.player1Name)
            self.winner = ""
            if(board != None):
                self.board = copy.deepcopy(board)
        else:
            self.againstAI = copy.deepcopy(game.againstAI)
            self.board  = copy.deepcopy(game.board)
            self.state = copy.deepcopy(game.state)
            self.player1Name = copy.deepcopy(game.player1Name)
            self.player2Name = copy.deepcopy(game.player2Name)
            self.turn = copy.deepcopy(game.turn)
            self.winner = copy.deepcopy(game.winner)
            
    def playGame(self):
        if(self.againstAI == False):
            while(self.state == "Unfinished"):
                print("___________________________________________________")
                print(self.turn, "it is your turn to play")
                self.printBoard()
                move = self.getMoves()
                self.makeMove(move[0],move[1])
                print("___________________________________________________")            
                
            print("The game has ended")
            self.printBoard()
            if(self.state == "Draw"):
                print("The result is a draw")   
            else:
                print("The winner of the game is:", self.winner)
        else:
            while(self.state == "Unfinished"):
                sys.stdout.flush()
                print("___________________________________________________")
                if(self.turn == "AI"):
                    self.printBoard()
                    sys.stdout.flush()
                    self.makeAIMove()
                else:
                    print(self.turn, "it is your turn to play")
                    self.printBoard()
                    move = self.getMoves()
                    self.makeMove(move[0],move[1])
                print("___________________________________________________")
            
            print("The game has ended")
            self.printBoard()
            if(self.state == "Draw"):
                print("The result is a draw")   
            else:
                print("The winner of the game is:", self.winner)
                
    #checks current state of the game        
    def checkGameState(self):
        self.checkX()
        self.checkO()
        if(self.state != "Win"):
            for x in range(0,3):
                for y in range(0,3):
                    if(self.board[x][y] == "#"):
                        self.state = "Unfinished"
                        return
            self.state = "Draw"
                        
    #checks if X won        
    def checkX(self):
        #check up left right
        for row in range(0,3):
            if(self.board[row][0] == "X"):
                if(self.board[row][0] == self.board[row][1]):
                    if(self.board[row][1] == self.board[row][2]):
                        self.winner = self.player1Name
                        self.state = "Win"
                        return
        #check up down
        for col in range(0,3):
            if(self.board[0][col] == "X"):
                if(self.board[0][col] == self.board[1][col]):
                    if(self.board[1][col] == self.board[2][col]):
                        self.winner = self.player1Name
                        self.state = "Win"
                        return
        #check diagonals
        if(self.board[0][0] == "X"):
            if(self.board[0][0] == self.board[1][1]):
                if(self.board[1][1] == self.board[2][2]):
                    self.winner = self.player1Name
                    self.state = "Win"
                    return                    
        
        if(self.board[0][2] == "X"):
            if(self.board[0][2] == self.board[1][1]):
                if(self.board[1][1] == self.board[2][0]):
                    self.winner = self.player1Name
                    self.state = "Win"
                    return
    #checks if O won   
    def checkO(self):
        #check up left right
        for row in range(0,3):
            if(self.board[row][0] == "O"):
                if(self.board[row][0] == self.board[row][1]):
                    if(self.board[row][1] == self.board[row][2]):
                        self.winner = self.player2Name
                        self.state = "Win"
                        return
        #check up down
        for col in range(0,3):
            if(self.board[0][col] == "O"):
                if(self.board[0][col] == self.board[1][col]):
                    if(self.board[1][col] == self.board[2][col]):
                        self.winner = self.player2Name
                        self.state = "Win"
                        return
        #check diagonals
        if(self.board[0][0] == "O"):
            if(self.board[0][0] == self.board[1][1]):
                if(self.board[1][1] == self.board[2][2]):
                    self.winner = self.player2Name
                    self.state = "Win"
                    return                    
        
        if(self.board[0][2] == "O"):
            if(self.board[0][2] == self.board[1][1]):
                if(self.board[1][1] == self.board[2][0]):
                    self.winner = self.player2Name
                    self.state = "Win"
                    return
        
    #switches turn of current player    
    def switchTurn(self):
        if(self.turn == self.player1Name):
            self.turn = self.player2Name
        else:
            self.turn = self.player1Name
            
     #adapted from http://inventwithpython.com/chapter10.html       
    def printBoard(self):
        print("The board is:")
        for x in range(0,3):
            print('', self.board[x][0],'|',self.board[x][1],'|',self.board[x][2])
            print('-----------')
        
    
    #check to see if want to play AI       
    def playAiCheck(self):
        againstAi = input("Would you like to play against AI? (Please enter Y or N)\n")
        while(againstAi.upper() != "Y" and againstAi.upper() != "N"):
            print("You entered \"",againstAi,"\" which is invalid, please enter a valid character")
            againstAi = input("Would you like to play against AI? (Please enter Y or N)\n")
        if(againstAi == "Y" or againstAi == "y"):
            self.againstAI = True
            first = input("User, would you like to play first? (Please enter Y or N)\n")
            while(first.upper() != "Y" and first.upper() != "N"):
                print("You entered \"",first,"\" which is invalid, please enter a valid character")
                first = input("User, would you like to play first? (Please enter Y or N)\n")            
            if(first.upper() == "Y"):
                 self.player1Name = input("Please enter your name: ")
                 self.player2Name = "AI"            
            else:          
                self.player1Name = "AI"
                self.player2Name = input("Please enter your name: ")
        
    #set player names from input
    def setNames(self):             
        if(self.againstAI == False):
            self.player1Name = input("Enter the name for player 1: \n")
            self.player2Name = input("Enter the name for player 2: \n")
        if(self.player1Name == ""):
            self.player1Name = "X"
        if (self.player2Name == ""):
            self.player2Name = "O"
            
    #print Player names
    def printPlayers(self):
        print("Player 1 is:", self.player1Name)
        print("Player 2 is:", self.player2Name)
        
    #returns current state ie - win, lose, draw, unfinished
    def getState(self):
        print("The current state of the game is:", self.state)
    
    #makes a move to the specifed row and column
    def makeMove(self,row,col):
        while(row > 3 or col > 3 or row < 1 or col < 1 ):
            print("Invalid Move")
            move = self.getMoves()
            row = move[0]
            col = move[1] 
        row = row-1
        col = col-1
        while(self.validateMove(row,col) == False):
            print("Invalid Move")
            move = self.getMoves()
            row = move[0]
            col = move[1] 
            row = row-1
            col = col-1
        row = row
        col = col
        if(self.turn == self.player1Name):
            self.board[row][col] = "X"
        else:
            self.board[row][col] = "O"
        self.checkGameState()
        self.switchTurn()
        
    #validates move to be within range and not occupied   
    def validateMove(self,row,col):
        if(self.board[row][col] != "#"):
            return False
        return True
    #gets the row and column from the user
    def getMoves(self):
        row = input("Please enter the row where you would like to play:\n")
        col = input("Please enter the column where you would like to play:\n")
        move = [int(row),int(col)]
        return move
    
    #utility for the AI
    def getAIUtility(self):
        if(self.state == "Draw"):
            return 0
        if(self.winner == "AI"):
            return 1
        return -1
    
    def getUserUtility(self):
        if(self.state == "Draw"):
            return 0
        if(self.winner != "AI"):
            return 1
        return -1
        
    #returns list of possible game states 
    def getActions(self):
        actions = []
        for x in range(0,3):
            for y in range(0,3):
                if(self.board[x][y] == "#"):
                   move = game(self)
                   move.makeMove(x+1,y+1)
                   actions.append(move)
        return actions
    
    #whether state is terminal or not    
    def isTerminal(self):
        return(self.state != "Unfinished")
    
    def makeAIMove(self):
        if(self.turn == "AI"):
            print("AI is playing...")
            print("HERE IS THE ALPHABETA SEARCH TREE:")
            ABT = AlphaBetaTree(self)
            temp = ABT.AlphaBetaSearch()            
            for x in range(0,3):
                for y in range(0,3):
                    if(self.board[x][y] != temp.board[x][y]):
                        self.makeMove(x+1,y+1)
                        return
class node: 
    def __init__(self, game,parent = None):
        self.game = game
        self.children = []
        self.parent = parent
        self.utility = 0
        self.visited = False
        
    def addChild(self,child):
        child.parent = self
        self.children.append(child)
    
class AlphaBetaTree:
    def __init__(self,game1):
        self.root = node(copy.deepcopy(game1))
        self.action = None
        self.buildTree(self.root)
        
    def buildTree(self,parent = None):        
        if(parent == None):
            parent = self.root            
        if(parent.game.isTerminal()):
            parent.utility = parent.game.getAIUtility()
            return        
        actions = parent.game.getActions()
        for a in actions:
            child = node(a,parent)
            parent.addChild(child)
            self.buildTree(child)
            temp = 55
            for x in parent.children:
                if(parent.game.turn == self.root.game.turn):
                    if(temp < x.utility or temp == 55):
                        temp = x.utility
                else:
                    if(temp > x.utility or temp == 55):
                        temp = x.utility
            parent.utility = temp
    
    def AlphaBetaSearch(self):
        temp = self.AlphaBetaMax(self.root, -1000,1000) 
        print("HERE IS THE UTILITY VALUE FOR MOVE CHOSEN:", temp)
        for child in self.root.children:
            if(child.utility == temp):
                return child.game        
        
    def AlphaBetaMax(self,node,alpha,beta):
        if(node.game.isTerminal()):
            print("Terminal node with utility value: ")
            node.game.printBoard()
            sys.stdout.flush()
            print(node.game.getAIUtility())
            sys.stdout.flush()
            print()
            sys.stdout.flush()
            return node.game.getAIUtility()
        node.game.printBoard()
        print()
        sys.stdout.flush()
        temp = -100        
        for action in node.children:
            temp = max(temp,self.AlphaBetaMin(action,alpha,beta))
            if(temp >= beta):
                return temp
            alpha = max(alpha,temp)
        return temp
        
    def AlphaBetaMin(self,node,alpha,beta):
        if(node.game.isTerminal()):
            print("Terminal node with utility value: ")
            node.game.printBoard()
            sys.stdout.flush()
            print(node.game.getAIUtility())
            print()
            sys.stdout.flush()
            return node.game.getAIUtility()
        
        node.game.printBoard()
        print()
        sys.stdout.flush()
        temp = 100        
        for action in node.children:
            temp = min(temp,self.AlphaBetaMax(action,alpha,beta))
            if(temp <= alpha):
                return temp
            beta = min(beta,temp)
        return beta   

    def getNumNodes(self):
        count = 0
        temp = queue.Queue()
        temp.put(self.root)
        while(temp.empty() == False):
            node = temp.get()
            if node.game.isTerminal():
                count += 1
            for x in node.children:
                temp.put(x)
        return count
ttt = game()
ttt.board = np.array([["X","#","#"],
                      ["O","#","#"],
                      ["X","O","X"]])
ttt.turn = "AI"
ttt.againstAI = True
ttt.printPlayers()
sys.stdout.flush()
print("HERE IS THE INITIAL STATE:")
ttt.printBoard()
sys.stdout.flush()
print("_________________________________________")
sys.stdout.flush()
ttt.makeAIMove()
sys.stdout.flush()
print("_________________________________")
print("AI HAS PLAYED HERE IS THE RESULTING STATE:")
sys.stdout.flush()
ttt.printBoard()

