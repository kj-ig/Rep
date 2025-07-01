'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "friends"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    col1 = [item[0] for item in board]
    col2 = [item[1] for item in board]
    col3 = [item[2] for item in board]
    dia1 = []
    dia2 = []
    dia1.append(board[0][0])
    dia1.append(board[1][1])
    dia1.append(board[2][2])
    if len(set(board[0])) == 1 and board[0][0] != "":
        return board[0][0]
    elif len(set(board[1])) == 1 and board[1][0] != "":
        return board[1][0]
    elif len(set(board[2])) == 1 and board[2][0] != "":
        return board[2][0]
    elif len(set(col1)) == 1 and col1[0] != "":
        return col1[0]
    elif len(set(col2)) == 1 and col2[0] != "":
        return col2[0]
    elif len(set(col3)) == 1 and col3[0] != "":
        return col3[0]
    elif len(board) == 3:
        dia2.append(board[0][2])
        dia2.append(board[1][1])
        dia2.append(board[2][0])
        if len(set(dia1)) == 1 and dia1[0] != "":
            return dia1[0]
        elif len(set(dia2)) == 1 and dia2[0] != "":
            return dia2[0]
        else:
            return "NO WINNER"
    elif len(board) > 3:
        col4 = [item[3] for item in board]
        if len(set(board[3])) == 1 and board[3][0] != "":
            return board[3][0]
        elif len(set(col4)) == 1 and col4[0] != "":
            return col4[0]
        elif len(board) == 4:
            dia1.append(board[3][3])
            dia2.append(board[0][3])
            dia2.append(board[1][2])
            dia2.append(board[2][1])
            dia2.append(board[3][0])
            if len(set(dia1)) == 1 and dia1[0] != "":
                return dia1[0]
            elif len(set(dia2)) == 1 and dia2[0] != "":
                return dia2[0]
            else:
                return "NO WINNER"
        elif len(board) > 4:
            col5 = [item[4] for item in board]
            if len(set(board[4])) == 1 and board[4][0] != "":
                return board[4][0]
            elif len(set(col5)) == 1 and col5[0] != "":
                return col5[0]
            elif len(board) == 5:
                dia1.append(board[4][4])
                dia2.append(board[0][4])
                dia2.append(board[1][3])
                dia2.append(board[2][2])
                dia2.append(board[3][1])
                dia2.append(board[4][0])
                if len(set(dia1)) == 1  and dia1[0] != "":
                    return dia1[0]
                elif len(set(dia2)) == 1 and dia2[0] != "":
                    return dia2[0]
                else:
                    return "NO WINNER"
            elif len(board) == 6:
                col6 = [item[5] for item in board]
                dia1.append(board[5][5])
                dia2.append(board[0][2])
                dia2.append(board[0][2])
                dia2.append(board[0][2])
                dia2.append(board[0][2])
                dia2.append(board[0][2])
                dia2.append(board[0][2])
                if len(set(board[5])) == 1 and board[5][0] != "":
                    return board[5][0]
                elif len(set(col6)) == 1 and col6[0] != "":
                    return col6[0]
                elif len(set(dia1)) == 1 and dia1[0] != "":
                    return dia1[0]
                elif len(set(dia2)) == 1 and dia2[0] != "":
                    return dia2[0]
                else:
                    return "NO WINNER"
            else:
                return "NO WINNER"
    else:
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    route = [key for key in route_map.keys()]
    start = [key[0] for key in route_map.keys()]
    end = [key[1] for key in route_map.keys()]
    first = 0
    second = 0
    result = 0
    for item in start:
        if first_stop != item:
            first += 1
        else:
            break
    for item in end:
        if second_stop != item:
            second += 1
        else:
            break
    index = abs(first - second)
    if first <= second:
        new = first + index
        while first < (new + 1):
            result += route_map[route[first]]["travel_time_mins"]
            first += 1
        return result
    elif first > second:
        new = first - index
        while first != new:
            result += route_map[route[first]]["travel_time_mins"]
            if first == (len(route_map) - 1):
                first += -first
                new += 1
            else:
                first += 1
        return result