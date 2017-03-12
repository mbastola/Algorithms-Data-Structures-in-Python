1. getSquare: O(n)as the function has to go over each row(in a for loop) to find a given row and get the desired charcter in the given column of that row.

2. getStartLocation: the if condition in this function is O(n)as it calls getSquare function.The two for loops above the if condition are O(n^2). Thus the given function is O(n^3).

3. getGoalLocation: the if condition in this function is also O(n)as it calls getSquare function.The two for loops above the if condition are O(n^2). Thus the given function is slso O(n^3).  

4. __str__: O(n) as the function has to go over each row(in a for loop) to find a given row and concatenate it to the srting.

5.solveMaze Setup:  setmaze = O(n^3)as it takes two for loops that runs through each rows and columsn respectively and within the for loops is an if condition that takes isGoal or isStart etc which themselves are O(n). Thus the entire function is O(n^3) 

6. solveMaze Neighbor check: The for loop is O(n)as it takes getSuqare method.The "if not in added" is a loop in disguise,and depend on 'n'. Thus the neibor check is O(n^2). 

7. solveMaze Neighbor loop: If the solvemaze neighbor check is O(n^2), then it has only one for loop(for locToCheck in toCheck) in it which is O(1) as it doesnt affect n in any ways. Thus iut should alos be O(n^2).

8. solveMaze Make path: In the case where it finds goal after every position checked , the while loop iterates over each and every position as the agenda will contain all position. If its unsolvable, then it returns empty list. It will be O(n^2).   

9. solveMaze Goal check: O(n) as isGoal is O(n).

10. solveMaze Main loop: the goal check is maximum O(n) when it finds a goal. Then while not self.__agenda.isEmpty()is O(n^2)as the agenda could have positions ranginf from 1 to n^2. Thus it is O(n^3)

11. solveMaze: O(n^3) as the setup part and solve maze takes O(n^3). 

part 2:
The unsolvable maze would be the hardest one where the functin would check every available positions(n*n). The graph looks cubic as expected. 

part 3: 

1.  GetSquare is now O(1) because it only indexes the list.

2.  getStartLocation is O(1) since the method  returns already found self.startlocation

3.  getEndLocation is O(1) since the method returns already found self.goallocation

4.  The __str__ is still O(1) since it returns self.mystr 

part 4: 

6. solveMaze Neighbor check: O(n)as now added wont depend on n.
7. solveMaze Neighbor loop: O(n)
8. solveMaze Make path: O(n^2)
9. solveMaze Goal check: O(1) as now isGoal is O(1)
