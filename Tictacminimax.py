###########################
### Author:Leyton Taylor###
### Date: 10/7/19       ###
### Class: CS3610       ###
###########################

import math


###Takes a current state of a Tic-Tac toe board###
###and returns the move you should do next###


##MainMethod
def main():
  
  inputBoardState=input("What is the current state of the Board? ")

  initState=list(inputBoardState)
  
  State=[initState[i:i+3] for i in range(0,9,3)]
  move= MiniMax(State,None, True,0)
  
  moveList=[]
  
  for i in range(len(move[1])):
    moveList.append(str(move[1][i][0]*3+(move[1][i][1])+1))
  
  
  if(move[0]>0):
    print("You should put pieces in positions" + " " + ' '.join(moveList)+"\n"+
          "And you will eventually win")
  else:
    print("You should put pieces in positions" + " " + ' '.join(moveList)+"\n"+
          "But you won't win:(")

###def play():
  
      

##Generates a List of Legal moves
##That can be applied to the State
def genLegalMoves(State):

  legalMoves=[]

  for i in range(len(State)):
    for j in range(len(State[0])):
      
      if(State[i][j]!="*"):
        legalMoves.append([(i,j)])

      if(i <2 and j<2):
        if(i==0):

          tempLegalMoves=list(filter(lambda x: isLegal(State,x), [[(i,j),(i+2,j)],[(j,i),(j, i+2)],[(j,0),(j,1),(j,2)],[(0,j),(1,j),(2,j)]]))
          
          for x in tempLegalMoves:
            legalMoves.append(x)

        tempLegalMoves=list(filter(lambda x: isLegal(State,x), [[(i,j),(i,j+1)],[(j,i),(j+1,i)]]))

        for x in tempLegalMoves:
          legalMoves.append(x)

      legalMoves=list(filter(None, legalMoves))


  return(legalMoves)  
                
      
##Returns true iff all of the moves in the
##Sequence are legal Moves
def isLegal(State, moveSequence):
  
  legalMove = True
  
  for move in moveSequence:
    
    if State[move[0]][move[1]]=="*":
      legalMove=False

  return legalMove


###Returns the Next state when 
##move is applied
def updateState(State, Event):
    if(Event!=None):
        for m in Event:
            State[m[0]][m[1]]="*"
    return(State)


##Returns (10-N)*playerMultiplier
##RWhere N = total Number of moves made so far
##Rand playerMultiplier = 1(MaxPlayer), -1(MinPlayer)

def eval(State, isMax, N):
  
  if(isMax==True):
    return((10-N)*1)
  else:
    return((10-N)*-1)


##Returns a boolean value of if the State
##is an end state
def isLeaf(State):
  return State==[["*","*","*"],["*","*","*"],["*","*","*"]]


##Recursive Algorithm for finding optimal move
##for Max or Min
def MiniMax(State, e, isMax, N):
  #print(N)

  s1 = updateState(State, e) 
  #print("isLeaf"+str(isLeaf(s1)))
  if (isLeaf(s1)): 
    #print("isMax"+str(isMax))
    #print(eval(s1,isMax,N))
    return eval(s1,isMax,N)

  if (isMax==True): 
    highest = -10 
    for e1 in genLegalMoves(s1):  
        tmp = MiniMax(s1, e1, False, N+1)    
        if (tmp > highest):
            highest = tmp
            move = e1            
    if(N!=0):
        return highest
    else:
        return highest, move
  else:
    lowest = 10
    for e1 in genLegalMoves(s1):
        tmp = MiniMax(s1, e1, True, N+1)    
        if (tmp < lowest):
            lowest = tmp
            move = e1
    if(N!=0):
        return lowest
    else:
        return lowest, move


if __name__ =="__main__":
  main()






