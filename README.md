### PART 1: THE 2021 PUZZLE

Problem given to us is to obtain goal state from the given state using the pre-defined rotations like particular 
row/column can rotate only in particular direction.

Pre-defined rotations given to us are:
* 1st and 3rd rows can rotate only in LEFT direction
* 2nd and 4th rows can rotate only in RIGHT direction
* 1st, 3rd and 5th columns can rotate only in UP direction
* 2nd and 4th columns can rotate only in DOWN direction

#### Problem statement
* Here, input will be given in form of 1-D array with 20 elements. We divided this into 4X5 2-D array with 4-Rows and 
  5-Columns. 
  
* Using the pre-defined rotations, our goal is to obtain goal state which is 
  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]. 

#### Successor function
* Here, we have implemented a successor function which takes current state as input and gives all possible next states 
  as output. 
  
* In the successor function, we have used in-built python rotate function to rotate the particular row/column in particular 
  direction. 
  
* We appended the rotation direction of child node along with the state while storing the successors, to provide the 
  output path if goal state is obtained.

#### Heuristic function
* Here, we have used cost evaluation function f(s) = h(s)+g(s) where h(s)-cost from current state to goal state 
  and g(s) is cost from initial state to current state.
  
* The heuristic(h(s)) we used in this problem is calculating the misplaced tiles at each state.
  g(s) is number of steps it to obtain from initial state to current state. 

* Here, misplaced tiles is admissible because it's value reduce everytime when we move to next state. 
  If we consider the manhattan distance as heuristic, it fails to be admissible for edge column values.
  (For the last column values, even though we can reach its goal position by one rotation.... manhattan distance will be 
  four instead of  one)


#### A brief description of how our search algorithm works:

* Here, our algorithm will take initial/given state as input. 
  
* We have created a fringe(Priority Queue) which will pop the priority element first. 
  
* Popped out element from fringe have 4 parameters. (cost evaluation value(h+g), current state, Direction to reach 
  current state, value of g)
  
* While fringe is not empty, will iterate through the elements in fringe and will check if goal state is obtained. 
  
* If it reached goal state, we will terminate the code and return the path/directions to reach goal state from initial 
  state. 
  
* Else, algorithm will find the successor states of current state using the successor function implemented and it will 
  append them to fringe.

#### Discussion of any problems faced, simplifications, and/or design decisions made.

* At the start, we have tried many heuristic functions like manhattan distance, Inversion count, Manhattan+Linear conflict. 

* But we got either wrong output or the program went in to infinite loop. 

* Also, we struggled with the successor function like how to rotate only one row/column and also in storing the path/direction.

* In the solver function, input is giving in form of tuple but we converted that data type into list for our operations 
  and simplicity. 
