The main() method in Tictacminimax.py will allow you to input different Test States 
For the board and will return the optimal move for any test state. 
Below the optimal move will tell you if you will eventually win or not. 
There is a test.py file as well with a couple of tester methods.

There is a List called TestStates[] which has multiple test states that I used to test my 
Code. 

legalMovesTest() returns a list of all possible moves for each state in TestStates[]

testIsLeaf() simply checks if a state is a leaf node or not

updateStateTest(state, move) takes two parameters, 
1) the Current State of the board
2) A sequence of moves of the form [(0,2),(1,2)],[(0,0)] for example.

All of my states are stored in my program as nested lists. 

For example “*********” would be [[“*”,”*”,”*”],[“*”,”*”,”*”],[“*”,”*”,”*”]]

To bypass the main method and test MiniMax directly 

You can call MiniMax(State,None,True,0) for any state of the form gave above.
The return value will be ((10-N)*PlayerMultiplier, The sequence of Moves to do in tuple form))
