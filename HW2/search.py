# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

from game import Directions
import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    print "start :",problem.getStartState()
    print problem.goal
    print "next :",problem.getSuccessors(problem.getStartState())
    print "cost :",problem.getCostOfActions([Directions.WEST])
    myqueue = util.PriorityQueue()
    goal = (0,0)
    myqueue.push(problem.getStartState(),1)
    visited ={problem.getStartState() : (None,None ,0)}
    while (myqueue.isEmpty()== False ):
        temp = myqueue.pop()
        # print temp
        if problem.isGoalState(temp):
            goal = temp
            break
        pchild= problem.getSuccessors(temp)
        for child in pchild:
            if child[0] not in visited:
                myqueue.push(child[0] , 1+visited[temp][2]+heuristic(child[0],problem))
                visited[child[0]]=(temp,child[1], 1+visited[temp][2])
        if (problem.isGoalState(goal)): 
            break
    path=[]

    while (goal != problem.getStartState()):
        path.append(visited[goal][1])
        goal = visited[goal][0]
    path.reverse()
    return path
    util.raiseNotDefined()


# Abbreviations
astar = aStarSearch
