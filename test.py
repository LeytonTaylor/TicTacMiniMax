import TicTacminimax



TestStates = [


	[["-","*","-"],["-","-","*"],["-","*","-"]],
	[["-","-","-"],["-","-","*"],["-","*","-"]],
	[["-","*","-"],["*","-","*"],["*","*","-"]],
	[["*","-","*"],["*","*","*"],["*","-","*"]],
	[["-","-","-"],["-","*","-"],["-","-","-"]],
	[["*","-","*"],["*","-","*"],["*","*","-"]],
	[["*","*","*"],["*","*","-"],["*","*","*"]],
        [["-","*","-"],["-","-","*"],["*","*","-"]],
        [["-","-","-"],["*","-","*"],["-","*","-"]],
        [["-","-","-"],["*","-","*"],["-","*","-"]],
        [["-","-","-"],["-","-","*"],["-","*","-"]],


        
	]


def legalMovesTest():
	LegalMovesList=[]
	for test in TestStates:
		LegalMovesList.append(TicTacminimax.genLegalMoves(test)+["Next LegalSequence"]+[])

	return(LegalMovesList)

def testIsLeaf():
        assert(True, TicTacminimax.isLeaf([["*","*","*"],["*","*","*"],["*","*","*"]]))


def updateStateTest(state,move):
        return TicTacminimax.updateState(State, move)
        

        

        
        

		



