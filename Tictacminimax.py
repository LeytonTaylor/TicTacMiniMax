###########################
### Author:Leyton Taylor###
### Date: 10/7/19		###
### Class: CS3610		###
###########################

import math

###Takes a current state of a Tic-Tac toe board###
###and returns the move you should do next###
class MiniMax():

	##Generates a List of Legal moves
	##That can be applied to the State
	def genLegalMoves(State):

		legalMoves=[]
		for i in range(len(State)-1):
			for j in range(len(State[0])-1):
				if(State[i][j]!="*"):
					legalMoves.append([(i,j)])

				if(i==0):
					
					legalMoves=[legalMoves.append(list(filter(lambda x: isLegal(State,x[0])+isLegal(State,x[1]), [[[(i,j),(i+2,j)],[(j,i),(j, i+2)]]])))]

				legalMoves=[legalMoves.append(list(filter(lambda x: isLegal(State,x[0])+isLegal(State, x[1]) + isLegal(State, x[2])+isLegal(State, x[3]),
					[[[(i,j),(i,j+1)],[(j,i),(j+1,i)],[(i,0),(i,1),(i,2)],[(0,i),(1,i),(2,i)]]])))]

		print(legalMoves)	
									
				


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
	def updateState(State, move):



	#Returns (10-N)*playerMultiplier
	##Where N = total Number of moves made so far
	##and playerMultiplier = 1(MaxPlayer), -1(MinPlayer)
	def eval(State):




	def MiniMax(State, move, isMax):

		
