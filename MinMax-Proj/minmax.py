import game


def max(grid, alpha, beta):
    maxvalue = -2
    maxmoveX = None
    maxmoveY = None
    result = game.game_result(game.board)
    if result is not None:
        if result == "X":
            return (1, 0 ,0)
        if result == "O":
            return (-1, 0, 0)
        if result == "draw":
            return (0, 0 ,0)


    for i in range(3):
        for j in range(3):
            if grid[i][j] is None:
                grid[i][j] = "X"
                (m, minI, minJ) = min(grid, alpha, beta)
                if(m > maxvalue):
                    maxvalue = m
                    maxmoveX = i
                    maxmoveY = j
                grid[i][j] = None

                if maxvalue >= beta:
                    return maxvalue, maxmoveX, maxmoveY

                if maxvalue > alpha:
                    alpha = maxvalue

    return maxvalue, maxmoveX, maxmoveY


def min(grid, alpha, beta):
    minvalue = 2
    moveX = None
    moveY = None
    result = game.game_result(game.board)
    if result is not None:
        if result == "X":
            return (1, 0, 0)
        if result == "O":
            return (-1, 0, 0)
        if result == "draw":
            return (0, 0, 0)

    for i in range(3):
        for j in range(3):
            if grid[i][j] is None:
                grid[i][j] = "O"
                (m, minI, minJ) = max(grid, alpha, beta)
                if (m < minvalue):
                    minvalue = m
                    moveX = i
                    moveY = j
                grid[i][j] = None

                if minvalue <= alpha:
                    return minvalue, moveX, moveY

                if minvalue < beta:
                    beta = minvalue

    return minvalue, moveX, moveY

