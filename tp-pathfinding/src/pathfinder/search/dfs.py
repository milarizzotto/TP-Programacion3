from src.pathfinder.models.grid import Grid
from src.pathfinder.models.frontier import StackFrontier
from src.pathfinder.models.solution import NoSolution, Solution
from src.pathfinder.models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        if grid.end == node.state:
            return Solution(node, explored)

        # Initialize the frontier with the initial node
        # In this case, the frontier is a stack
        frontier = StackFrontier()
        frontier.add(node)

        while True:

            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored)

            # Remove a node from the frontier
            node = frontier.remove()

            # Move
            if node.state in explored:
                continue
            explored[node.state] = True
            for action, position in grid.get_neighbours(node.state).items():
                print(action, position)
                new_state = position
                if new_state not in explored:
                    new_node = Node("", new_state, node.cost + grid.get_cost(new_state), node, action)
                    if grid.end == new_node.state:
                        return Solution(new_node, explored)
                    frontier.add(new_node)