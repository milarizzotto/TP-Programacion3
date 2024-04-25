from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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
        explored[node.state] = 0

        # Initialize the frontier with the initial node
        # In this example, the frontier is a PriorityQueue
        frontier = PriorityQueueFrontier()
        frontier.add(node,0)

        while True:

            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored)

            # Remove a node from the frontier
            node = frontier.pop()
            if grid.end == node.state:
                return Solution(node,explored)
            # Move
            for action in grid.get_neighbours(node.state).items():
                new_state = action[1]
                cost = node.cost + grid.get_cost(new_state)
                if new_state not in explored or cost < explored[new_state]:
                    new_node = Node("",new_state,cost,node,action[0])
                    explored[new_node.state] = cost
                    frontier.add(new_node,cost)
