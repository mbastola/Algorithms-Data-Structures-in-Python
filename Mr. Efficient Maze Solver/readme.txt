no4)
In Stack Agenda, because of using Linked lIsts with O(1) efficiency in PopFront and pushFront method, the push and pop are O(1) and thus its efficient in complexity. In worst case since every path is searched, this is efficient.

In QUEUE Agenda, because of using Linked lIsts with O(1) efficeincy in PopFront and pushBack method, the enqueue and dequeue are O(1) and thus its efficient.

The PriorityQueue Agenda uses a MinPriority Queue. For getItem method, the dequeue method of the min Priority Queue which is nlog(n). The addItem is also O(nlogn). Hence it is quite expensive than both stack n queue agendas in terms of enqueuing and dequeing.

No. The priority queue wont always give us the shortest path. It calculates the displacement between each location aand goal but it neednt be the shortest disatance as long as we dont consider every path we cannot specify which one was shortest. As in Manhattan, you calculate shortest route but if there exist buildings in between then u are stuck and then have to figure out next shortest route. Had we checked each route beforehand,we could know the shortest route without blocks.for eg,

8 8
........
....#.#.
....#...
....#*#.
...#..#.
..#..#..
.#..#...
o.......

Pririty queue is best at more wall less mazes. For eg.

8 8
.......o
........
........
........
........
........
........
.......*

in above maze the stack will check each line and then end up, the queue with find the shortest path but will check more number of paths. But the priority queue with find it fast and in direct sense at most half.

8 8
........
....#.#.
....#...
....#*#.
...#..#.
..#..#..
.#..#...
o..#....

in above maze, priority queue fails drastically, the stack takes less than half number of path.

no 6) The worst case would be quite equivalent to Priority queue as the enqueue and dequeue are similar. Less efficient than stack and queue based agendas.

The A* takes goal loc as well as its current loc into account and add them up.So it will always be aware of its position and the remaining position with goal Loc. if any other position is better or shortest, it will take that position into account as that position will have lesser priority. Hence it will always give shortest location.

8 8
........
......#.
.... #..
....#...
...#.*#.
..#..#..
.#..#...
o..#....

In above type of mazes, the A* will have better results. It uses less than half locations than mere Manhattan distance.

10 10
o.........
.########.
........#.
...###..#.
...#*#..#.
...#.#..#.
...#.#..#.
...#.#..#.
...#.####.
...#......

in above maze, the A* fails.. Stack agenda perfroms better as it searches less than half locations.













