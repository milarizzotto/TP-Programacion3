from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

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
        # In this example, the frontier is a queue
        frontier = QueueFrontier()
        frontier.add(node)

        while True:

            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored)

            # Remove a node from the frontier
            node = frontier.remove()

            # Move
            for action in grid.get_neighbours(node.state).items():
                #print(action)
                new_state = action[1]
                if new_state not in explored:
                    new_node = Node("",new_state,node.cost + grid.get_cost(new_state),node,action[0])
                    if grid.end == new_node.state:
                        return Solution(new_node,explored)
                    explored[new_node.state] = True
                    frontier.add(new_node)
