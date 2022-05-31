#!/usr/bin/env python
# coding: utf-8

# ###### Item 1.
#     Relationship Status. 10 points.
#     Let us pretend that you are building a new app.
#     Your app supports social media functionality, which means that users can have
#     relationships with other users.
#     There are two guidelines for describing relationships on this social media app:
#     1. Any user can follow any other user.
#     2. If two users follow each other, they are considered friends.
#     This function describes the relationship that two users have with each other.
#     Please see "assignment-2-sample-data.py" for sample data. The social graph
#     will adhere to the same pattern.
#     Parameters
#     ----------
#     from_member: str
#         the subject member
#     to_member: str
#         the object member
#     social_graph: dict
#         the relationship data    
#     Returns
#     -------
#     str
#         "follower" if fromMember follows toMember,
#         "followed by" if fromMember is followed by toMember,
#         "friends" if fromMember and toMember follow each other,
#         "no relationship" if neither fromMember nor toMember follow each other.
#     '''
#     # Write your code below this line

# In[3]:


social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}


# In[76]:


from_member = input(str("Enter first username:"))

from_following = (social_graph[from_member]["following"])


to_member = input(str("Enter second username:"))
to_following = (social_graph[to_member]["following"])


def relationship_status(social_graph):
    if to_member in from_following and from_member in to_following:
        return "friends"
    if to_member in from_following:
        return "follower"
    if from_member in to_following:
        return "followed by"
    else:
        return "no relationship"

print(relationship_status(from_member))


# ###### def tic_tac_toe(board):
#     '''
#     Item 2.
#     Tic Tac Toe. 10 points.
#     Tic Tac Toe is a common paper-and-pencil game. 
#     Players must attempt to successfully draw a straight line of their symbol across a grid.
#     The player that does this first is considered the winner.
#     This function evaluates a tic tac toe board and returns the winner.
#     Please see "assignment-2-sample-data.py" for sample data. The board will adhere
#     to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
#     have more than one winner. The board will only ever have 2 unique symbols at the same time.
#     Parameters
#     ----------
#     board: list
#         the representation of the tic-tac-toe board as a square list of lists
#     Returns
#     -------
#     str
#         the symbol of the winner or "NO WINNER" if there is no winner
#     '''
#     # Write your code below this line

# In[70]:


board = [
['X','X','O'],
['O','X','X'],
['O','X','O'],
]

def row(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def diagonal(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0

column_board = [list(i) for i in zip(*board)]

def tic_tac_toe(board):
    for column in column_board:
        win = row(column_board) or diagonal(board)
        if win:
            return win
        else:
            return "No Winner"

print(tic_tac_toe(board))


# ###### def eta(first_stop, second_stop, route_map):
#     '''
#     Item 3.
#     ETA. 10 points.
#     A shuttle van service is tasked to travel along a predefined circlar route.
#     This route is divided into several legs between stops.
#     The route is one-way only, and it is fully connected to itself.
#     This function returns how long it will take the shuttle to arrive at a stop
#     after leaving another stop.
#     Please see "assignment-2-sample-data.py" for sample data. The route map will
#     adhere to the same pattern. The route map may contain more legs and more stops,
#     but it will always be one-way and fully enclosed.
#     Parameters
#     ----------
#     first_stop: str
#         the stop that the shuttle will leave
#     second_stop: str
#         the stop that the shuttle will arrive at
#     route_map: dict
#         the data describing the routes
#     Returns
#     -------
#     int
#         the time it will take the shuttle to travel from first_stop to second_stop
#     '''
#     # Write your code below this line
# 

# In[80]:


legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

first_stop = input(str("Enter first stop:"))
second_stop = input(str("Enter destination:"))


eta = 0
destination_holder = "" 
arrived = False 

while arrived == False: 
    for x in legs:
        if x[0] == first_stop:
            if x[1] == second_stop:
                eta += legs[x]["travel_time_mins"]
                arrived = True
                break
            else:
                eta += legs[x]["travel_time_mins"]
                destination_holder = x[1]
                print
        if x[0] == destination_holder:
            if x[1] == second_stop:
                eta += legs[x]["travel_time_mins"]
                arrived = True
                break
            else:
                eta += legs[x]["travel_time_mins"]
                destination_holder = x[1]
                
print(int(eta),"minutes")


# In[ ]:




