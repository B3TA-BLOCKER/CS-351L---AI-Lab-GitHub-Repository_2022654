import heapq  # Importing heapq to implement the priority queue for A* algorithm
import random  # Importing random to place the treasure, ghosts, and rewards randomly


# Function to create a maze grid with ghosts, safe zones, rewards, and a treasure
def create_haunted_maze_with_rewards(size, wall_prob, num_rewards):
    grid = [[' ' for _ in range(size)] for _ in range(size)]  # Create an empty grid filled with spaces
    grid[0][0] = 'S'  # 'S' marks the starting point at the top-left corner (0,0)

    # Randomly place walls based on the given probability
    for x in range(size):
        for y in range(size):
            if (x, y) != (0, 0):  # Ensure the start 'S' is not overwritten
                if random.random() < wall_prob:  # Decide whether to place a wall based on probability
                    grid[x][y] = '👻'


    # rewards ('🌟') at random positions
    rewards = []
    for _ in range(num_rewards):
        reward_x, reward_y = random.randint(0, size-1), random.randint(0, size-1)
        while grid[reward_x][reward_y] in ['S', 'T', 'X', 'G', 'Z', 'R']:
            reward_x, reward_y = random.randint(0, size-1), random.randint(0, size-1)
        grid[reward_x][reward_y] = '🌟'
        rewards.append((reward_x, reward_y))

      
    # For Exiting the maze
    treasure_x, treasure_y = random.randint(0, size-1), random.randint(0, size-1)
    while (treasure_x, treasure_y) == (0, 0) or grid[treasure_x][treasure_y] == 'X':
        treasure_x, treasure_y = random.randint(0, size-1), random.randint(0, size-1)
    grid[treasure_x][treasure_y] = '🚪' 

    return grid, (treasure_x, treasure_y), rewards


# Function to check if a position is valid (within bounds, not blocked by a wall, or occupied by a ghost)
def is_valid_position(grid, x, y):
    size = len(grid)
    return 0 <= x < size and 0 <= y < size and grid[x][y] != '👻'  # Return true if position is valid


# Heuristic function: Calculates the Manhattan distance between the current node and the goal
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance


# A* algorithm function to maximize rewards and avoid ghosts
def a_star_with_rewards(grid, start, goal):
    size = len(grid)
    open_list = []
    heapq.heappush(open_list, (0, start))  # Add the start node with priority 0

    g_score = {start: 0}  # Cost from start to current node
    parent = {start: None}  # To reconstruct the path

    # Dictionary to store maximum reward achievable from each position
    reward_score = {start: 0}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible directions: up, down, left, right

    while open_list:
        _, current = heapq.heappop(open_list)  # Get the node with the lowest f(n)

        if current == goal:
            break

        for direction in directions:
            next_x = current[0] + direction[0]
            next_y = current[1] + direction[1]
            next_state = (next_x, next_y)

            if is_valid_position(grid, next_x, next_y):
                tentative_g_score = g_score[current] + 1
                current_reward_score = reward_score[current]

                # Update reward score if the new position has a reward
                if grid[next_x][next_y] == '🌟':
                    current_reward_score += 1  # Increment reward score
                reward_score[next_state] = current_reward_score

                if next_state not in g_score or tentative_g_score < g_score[next_state]:
                    g_score[next_state] = tentative_g_score
                    f_score = tentative_g_score + heuristic(next_state, goal) - reward_score[next_state]
                    heapq.heappush(open_list, (f_score, next_state))
                    parent[next_state] = current

    # Reconstruct the path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        if current in parent:
            current = parent[current]
        else:
            print("No path found.")
            return []

    path.reverse()
    return path



# Function to print the grid with lines and the path marked
def print_grid_with_path(grid, path):
    grid_with_path = [row.copy() for row in grid]
    for (x, y) in path:
        if grid_with_path[x][y] not in ['S', 'T', 'G', 'Z', 'R']:  # Don't overwrite start 'S', treasure 'T', ghosts 'G', safe zones 'Z', and rewards 'R'
            grid_with_path[x][y] = '*'  # Mark the path with '*'

    print("\nGrid with Path:")
    print('-' * (len(grid_with_path) * 4 + 1))
    for row in grid_with_path:
        print('| ' + ' | '.join(row) + ' |')
        print('-' * (len(grid_with_path) * 4 + 1))


# Main function to play the game
def haunted_maze_escape_with_rewards():
    size = int(input("Enter the grid size (e.g., 6 for a 6x6 grid): "))
    wall_prob = 0.3
    num_rewards = int(input("Enter the number of rewards: "))

    grid, goal, rewards = create_haunted_maze_with_rewards(size, wall_prob, num_rewards)

    print("\nInitial Grid:")
    print_grid_with_path(grid, [])

    print("\nSearching for the treasure using A* algorithm...\n")
    path = a_star_with_rewards(grid, (0, 0), goal)

    print("\nPath to the Treasure with Maximum Rewards:")
    print_grid_with_path(grid, path)

    print("\nRewards Collected:")
    collected_rewards = sum(1 for (x, y) in rewards if (x, y) in path)
    print(f"Total Rewards Collected: {collected_rewards}")


# Run the game
haunted_maze_escape_with_rewards()
