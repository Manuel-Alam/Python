import maze_helper


def dfs(maze, current_point, explored):
    explored.append(current_point)

    if(maze_helper.symbol_at(maze, current_point) == "X"):

        explored.pop(0)
        for i in explored:
            maze_helper.add_walk_symbol(maze, i)

        maze_helper.print_maze(maze)

    if(maze_helper.symbol_at(maze, current_point) != "X"):

        for i in maze_helper.get_adjacent_positions(maze, current_point):
            if(i not in explored):
                dfs(maze, i, explored)
                explored.remove(i)

def main():
    maze = maze_helper.sample_maze()
    list = []

    #maze_helper.print_maze(maze)
    print("\nPrinting the maze, after solution found:")
    dfs(maze, (5,0), list)



if __name__ == '__main__':
    main()







