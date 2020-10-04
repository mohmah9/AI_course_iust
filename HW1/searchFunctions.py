import util

from game import Directions
from pacman import GameState as GS

UNREACHABLE_GOAL_STATE = [Directions.STOP]

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    return [s, s, w, s, w, w, s, w]

#### SOAL 3

def my_bfs(problem,START,mainpath):
    myqueue = util.Queue()
    goal = (0,0)
    depth = 1
    stop={}
    myqueue.push(START)
    visited ={START : (None,None,1)}
    while (myqueue.isEmpty()== False):
        temp = myqueue.pop()
        
        if problem.isGoalState(temp):
            goal = temp
            break
        pchild= problem.getNextStates(temp)
        for child in pchild:
            if child[0] not in visited:
                myqueue.push(child[0])
                visited[child[0]]=(temp,child[1])
        if (problem.isGoalState(goal)): 
            break
    path=[]
    if (stop == visited):
        return UNREACHABLE_GOAL_STATE
    stop=visited.copy()
    while (goal != START):
        path.append(visited[goal][1])
        # path_num.append(visited[goal][0])
        goal = visited[goal][0]
    path.reverse()
    for i in path :
        mainpath.append(i)
def bfs(problem):
    """
        Q3: BFS
    """
    path=[]
    # path_num=[]
    START=problem.getStartState()
    my_bfs(problem,START,path)
    print path
    # print path_num
    for i in range (len(problem.traverse_points)):
        my_bfs(problem,problem.traverse_points[problem.pos-1],path)
    return path

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
#####SOAL 1
def iddfs(problem):
    goal = (0,0)
    depth = 1
    stop = {}
    visited ={problem.getStartState() : [None,None,0,False]}
    while True:
        mystack = util.Stack()
        for i in visited.keys():
            visited[i][3]=False
        mystack.push(problem.getStartState())
        while (mystack.isEmpty()== False ):
            temp = mystack.pop()
            if problem.isGoalState(temp):
                goal = temp
                break
            pchild= problem.getNextStates(temp)
            for child in pchild:
                if (child[0] not in visited or visited[child[0]][3] ==False) and visited[temp][2]+1 <= depth:
                    mystack.push(child[0])
                    if child[0] in visited.keys() and not visited[child[0]][3]:
                        visited[child[0]][3]=True
                    else:
                        visited[child[0]]=[temp,child[1],visited[temp][2]+1,True]
        
        path=[]

        if (problem.isGoalState(goal)): 
            break
        depth+=1
        if (stop == visited):
            return UNREACHABLE_GOAL_STATE
        stop = visited.copy()

    while (goal != problem.getStartState()):
        path.append(visited[goal][1])
        goal = visited[goal][0]
    path.reverse()
    return path

##### SOAL 2
def dfs(problem, START , END ,mainpath):
    myqueue = util.Queue()
    goal = (0,0)
    depth = 1
    stop={}
    myqueue.push(START)
    visited ={START : (None,None)}
    while (myqueue.isEmpty() == False):
        temp = myqueue.pop()
        if END =="END":
            if problem.isGoalState(temp):
                goal = temp
                break
        else:
            if temp ==END:
                goal = temp
                break
        pchild= problem.getNextStates(temp)
        for child in pchild:
            if child[0] not in visited:
                myqueue.push(child[0])
                visited[child[0]]=(temp,child[1])
        if END=="END":
            if problem.isGoalState(temp):
                    goal = temp
                    break
        else:
            if goal == END: 
                break
    if (stop == visited):
        return UNREACHABLE_GOAL_STATE
    stop = visited
    path=[]
    while (goal != START):
        path.append(visited[goal][1])
        goal = visited[goal][0]
    path.reverse()
    for node in path:
        mainpath.append(node)
def is_goal(problem , state2 , corners):
    state = problem.getNextStates(state2)
    if len(state) == 2 :
        if (state[0][1]=="North" and state[1][1]!="South") or (state[0][1]=="South" and state[1][1]!="North") or (state[0][1]=="West" and state[1][1]!="East") or (state[0][1]=="East" and state[1][1]!="West"):
            corners.append(state2)
            return True
def corner_finder(problem , START , corners):
    myqueue = util.Queue()
    goal = (0,0)
    depth = 1
    stop={}
    myqueue.push(START)
    visited ={START : (None,None)}
    while (myqueue.isEmpty() == False):
        temp = myqueue.pop()
        is_goal(problem , temp , corners)
        pchild= problem.getNextStates(temp)
        for child in pchild:
            if child[0] not in visited:
                myqueue.push(child[0])
                visited[child[0]]=(temp,child[1])
    if (stop == visited):
        return UNREACHABLE_GOAL_STATE
def hide_and_seek(problem):
    first = True
    corners=[]
    path=[]
    START = problem.getStartState()
    corner_finder(problem ,START, corners)
    print corners
    for i in range(len(corners)):
        if first == True:
            dfs(problem , START ,corners[i] , path)
            first=False
        else:
            dfs(problem , corners[i-1] ,corners[i] , path)
    dfs(problem , corners[i] ,"END" , path)
    return path

####SOAL 4
def ucs(problem):
    """
    Q4: Search the node of least total cost first.
    """
    myqueue = util.PriorityQueue()
    goal = (0,0)
    depth = 1
    stop={}
    myqueue.push(problem.getStartState(),problem.cost_function(problem.getStartState()))
    visited ={problem.getStartState() : (None,None)}
    while (myqueue.isEmpty()== False ):
        temp = myqueue.pop()
        # print problem.cost_function(temp)
        if problem.isGoalState(temp):
            goal = temp
            break
        pchild= problem.getNextStates(temp)
        for child in pchild:
            if child[0] not in visited:
                myqueue.push(child[0] , problem.cost_function(child[0]))
                visited[child[0]]=(temp,child[1])
        if (problem.isGoalState(goal)): 
            break
    path=[]
    if (stop == visited):
        return UNREACHABLE_GOAL_STATE

    while (goal != problem.getStartState()):
        path.append(visited[goal][1])
        goal = visited[goal][0]
    path.reverse()
    return path
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
