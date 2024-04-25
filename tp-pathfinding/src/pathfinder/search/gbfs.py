from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

#Definir una funcion heuristica
def heuristica(node, objetivo):
    distancia_x = abs(node.state[0] - objetivo[0])
    distancia_y = abs(node.state[1] - objetivo[1])
    distancia = distancia_x + distancia_y
    return distancia

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = True
        
        # Initialize the frontier with the initial node
        # In this example, the frontier is a Priority Queue Frontier
        frontier = PriorityQueueFrontier()
        frontier.add(node, heuristica(node, grid.end)) #grid.end es la posicion objetivo

        while True:
            
            #  Fail if the frontier is empty

            if frontier.is_empty():
                return NoSolution(explored)
            
            # Remove a node from the frontier
            node = frontier.pop()

            if node.state == grid.end:
                return Solution(node, explored)

            for action in grid.get_neighbours(node.state).items():
                new_state = action[1]
                cost = node.cost + grid.get_cost(new_state)
                if new_state not in explored or cost < explored[new_state]:
                    new_node = Node("",new_state,cost)
                    explored[new_state] = cost
                    frontier.add(new_node,heuristica(new_node, grid.end))

            
        
