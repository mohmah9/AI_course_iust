# multiAgents.py
# --------------
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

from copy import deepcopy
from util import manhattanDistance
from game import Directions
import random
import util
import math

from game import Agent
from ghostAgents import GHOST_AGENT_MAX_DEPTH, GhostAgent


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()


class AdversarialSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxAgent, SmartPacmanAgent, SmartGhostAgent

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # index should be 0 by default
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

    def getOpponentIndex(self):
        return 1 - self.index


class MinimaxAgent(AdversarialSearchAgent):

    def getAction(self, gameState):
        """
        The Agent will receive a GameState and
        must return an action from Directions.{North, South, East, West, Stop}
        """
        minimaxScores = []
        legalActions = gameState.getLegalActions(self.index)
        for action in legalActions:
            score = self.minimax(
                gameState.generateSuccessor(self.index, action),
                self.getOpponentIndex(),
                0
            )
            minimaxScores.append((score, action))
        for i in minimaxScores:
            if i[1]=="Stop":
                minimaxScores.remove(i)
        bestAction = max(minimaxScores)[1]

        return bestAction

    def minimax(self, gameState, maximizingAgent, currentDepth):

        try:
            if self.evaluationFunction(gameState)==gameState.getScore():
                typee="min"
            else:
                typee="max"
        except:
            typee="min"
        a = self.my_minimax(gameState,maximizingAgent,currentDepth,typee)

        return a

    def my_minimax(self, gameState, maximizingAgent, currentDepth,status):
        if(self.depth == currentDepth or gameState.isWin() or gameState.isLose() or self.depth == 0):
            return self.evaluationFunction(gameState)

        if(maximizingAgent == self.index):
            opponent = self.getOpponentIndex()
        else:
            opponent = self.index
        nextt = []
        actions = gameState.getLegalActions(opponent)
        for action in actions:
            nextt.append(gameState.generateSuccessor(opponent,action))
        scores = []
        if(status == "min"):
            for state in nextt:
                scores.append(self.my_minimax(state,opponent,currentDepth+1,"max"))
            if(scores):
                return min(scores)
        else:
            for state in nextt:
                scores.append(self.my_minimax(state,opponent,currentDepth+1,"min"))
            if(scores):
                return max(scores)    


class SmartPacmanAgent(MinimaxAgent):
    def __init__(self, depth='2'):
        self.index = 0
        self.depth = int(depth)

    @staticmethod
    def evaluationFunction(gameState):
        # counter of foods
        numberOfFoodsLeft=gameState.getNumFood()
        # time
        currentScore = scoreEvaluationFunction(gameState)
        # fasele of ghost
        ghost_pacman = manhattanDistance(gameState.getPacmanPosition(),gameState.getGhostPosition(1))
        # fasele of foodscurrentGameState
        closestfood=0
        median=0
        temp_median=[]
        currentFood = gameState.getFood()
        x=-1
        for i in currentFood:
            x+=1
            for y in range(len(i)):
                if (currentFood[x][y]==True):
                    temp_median.append(manhattanDistance(gameState.getPacmanPosition(),(x,y)))
        try:
            median = sum(temp_median) / len(temp_median)
            closestfood=min(temp_median)
        except ValueError and ZeroDivisionError:
            pass
            
        score = -(2)* closestfood +(6)* ghost_pacman -(1)* numberOfFoodsLeft +(5)* currentScore
        # print("state" , gameState.getGhostStates())
        """
        Returns evaluation score for each gameState

        Args:
            gameState: an instance of pacman.GameState


        Returns:
            Return the evaluation score
        """
        
        return score

        # return score
        # util.raiseNotDefined()


class SmartGhostAgent(MinimaxAgent):
    def __init__(self, index):
        self.index = 1
        self.depth = GHOST_AGENT_MAX_DEPTH

    @staticmethod
    def evaluationFunction(gameState):
        """
        Similar to SmartPacmanAgent
        """
        util.raiseNotDefined()


class SuperGhostAgent(GhostAgent):
    def __init__(self, index):
        self.index = index
        self.depth = GHOST_AGENT_MAX_DEPTH

    def getAction(self, gameState):
        """
        The Agent will receive a GameState and
        must return an action from Directions.{North, South, East, West}
        """
        util.raiseNotDefined()
