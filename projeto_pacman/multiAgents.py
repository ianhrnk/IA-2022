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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn="scoreEvaluationFunction", depth="2"):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.getNextState(agentIndex, action):
        Returns the child game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        def minimax(gameState, agent, depth):
            if depth == 0 or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)

            if agent == 0:
                actions = {}
                for action in gameState.getLegalPacmanActions():
                    actions[action] = minimax(
                        gameState.generateSuccessor(0, action), agent + 1, depth - 1
                    )
                if depth == self.depth * gameState.getNumAgents():
                    return max(actions, key=actions.get)
                else:
                    return max(actions.values())
            else:
                actions = {}
                for action in gameState.getLegalActions(agent):
                    actions[action] = minimax(
                        gameState.generateSuccessor(agent, action),
                        0 if agent == gameState.getNumAgents() - 1 else agent + 1,
                        depth - 1,
                    )
                return min(actions.values())

        return minimax(gameState, 0, self.depth * gameState.getNumAgents())


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        def alphabeta(gameState, agent, depth, alpha, beta):
            if depth == 0 or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)

            if agent == 0:
                bestValue = float("-inf")
                actions = {}
                for action in gameState.getLegalPacmanActions():
                    actions[action] = alphabeta(
                        gameState.generateSuccessor(0, action),
                        agent + 1,
                        depth - 1,
                        alpha,
                        beta,
                    )
                    bestValue = max(bestValue, actions[action])
                    alpha = max(alpha, bestValue)
                    if beta <= alpha:
                        break
                if depth == self.depth * gameState.getNumAgents():
                    return max(actions, key=actions.get)
                else:
                    return bestValue
            else:
                bestValue = float("inf")
                for action in gameState.getLegalActions(agent):
                    value = alphabeta(
                        gameState.generateSuccessor(agent, action),
                        0 if agent == gameState.getNumAgents() - 1 else agent + 1,
                        depth - 1,
                        alpha,
                        beta,
                    )
                    bestValue = min(bestValue, value)
                    beta = min(beta, value)
                    if beta < alpha:
                        break
                return bestValue

        return alphabeta(
            gameState,
            0,
            self.depth * gameState.getNumAgents(),
            float("-inf"),
            float("inf"),
        )


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        def expectimax(gameState, agent, depth):
            if depth == 0 or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)

            if agent == 0:
                actions = {}
                for action in gameState.getLegalPacmanActions():
                    actions[action] = expectimax(
                        gameState.generateSuccessor(0, action), agent + 1, depth - 1
                    )
                if depth == self.depth * gameState.getNumAgents():
                    return max(actions, key=actions.get)
                else:
                    return max(actions.values())
            else:
                value = 0
                actions = gameState.getLegalActions(agent)
                for action in actions:
                    probability = 1 / len(actions)
                    value += probability * expectimax(
                        gameState.generateSuccessor(agent, action),
                        0 if agent == gameState.getNumAgents() - 1 else agent + 1,
                        depth - 1,
                    )
                return value

        return expectimax(gameState, 0, self.depth * gameState.getNumAgents())


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviation
better = betterEvaluationFunction
