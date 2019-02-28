# Random-Maze-Generator
## Get start
***·Exhibition of works***
### ![image](D:\Py1\GIF.gif) ###

***·requirements***
### 
    numpy=1.15.0
    opencv-python 
    
***·operating principle***



From the starting point to the end point, find a path through the BFS, that is, determine a point first, find the point connected to it for the current point, and finally find a path from the point it connects to the end point. The condition for reaching the border is that the point it connects to is the end point.

Write the mathematical equation as P_v = V+ P_j(V and J have side connections)

Immediately following if J = end, return; Since it is recursive, the return is not over, and all the way back to find the starting point, this road will not be repeated.


***·pseudocode***

 path=[]
 
 flag=false
 
 bfs（i）：
 
    if i上下左右有打印过：
            return
        print（i）  
        if Flag == false；
            path.append（i）
        if i == end；
            Flag = True
            
   bfs（i上下左右）  
   

  
