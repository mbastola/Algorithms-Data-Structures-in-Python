#Simple Maze Solver

maze-file4.txt is the maze where QueueAgenda is inefficient and StackAgenda is efficient.

maze-file5.txt is the maze where QueueAgenda is efficient and StackAgenda is inefficient.

The StackAgenda is a class that is based on first in last out principle. Thus, if it takes the real pathway later then goes along that path and doesnt wander around the other paths. The advantage of this charcteristics is that in the maze files with less alternate routes, this class work efficiently as it doesnt wander much around other unnecessary paths.Such as in maze-file4.

On the other hand, Queue agenda follows First in First Out principle. If it reaches a junction, then it adds both the paths(lets say a first and then b) and pops the item that went in first (i.e. a). Again for the popped item 'a' it checks the paths and adds them in. Now since its FILO, it then pops out 'b' and then looks for its paths. Therefore it takes into account every possible alternate pathways. The advantage is that it works good in the mazes with long alternative routes(such as maze-file5.txt) as it simultaneously checks every pathways but isnt that efficient where there is a good route without much alternate possible ways as it takes every path way into account which is in a sense, more time & memory consuming.
