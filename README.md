# Random-Maze-Generator

## Get start

***·Exhibition of works***

### ![image](https://github.com/baiyewww/Random-Maze-Generator/blob/master/imgs/GIF.gif) ###

***·requirements***

```
    numpy=1.15.0
    opencv-python 
```

***·usage***

```
$ python random_maze --width <width> --height <height> --unitsize <unitsize> --start <start> --end <end>
```

Default config:

* width = 30, the row contains 30 units
* height = 30, the col contains 30 units
* unitsize = 10, the size of unit is 10*10 pixel
* start = (0, 0), the beginning point is (0, 0)
* end = (29, 29),  the destination point is (29, 29)


***·procedure***

> Step1: Initialize the basic canvas by OpenCV

> Step2: Initialize the basic draw-line function by OpenCV

> Step3: Find a random path from the \<start\>to the \<end\>

> Step4: Use draw-line function and show the dynamic processing according to the path

> Step5: Traverse all units and randomly build the wall in four directions, and avoid the path

    
***·operating principle***



From the starting point to the end point, find a path through the BFS, that is, determine a point first, find the point connected to it for the current point, and finally find a path from the point it connects to the end point. The condition for reaching the border is that the point it connects to is the end point.

Write the mathematical equation as P_v = V+ P_j(V and J have side connections)

Immediately following if J = end, return; Since it is recursive, the return is not over, and all the way back to find the starting point, this road will not be repeated.


***·pseudocode***


BFS:

```
path = []
flag = False

bfs(i):
    if i has been visited:
        return
    visit i
    if Flag == False:
        path.append(i)
    if i == end:
        Flag = True

```

   

  
