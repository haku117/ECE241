from pythonds.graphs import Graph
from knightGraph import knightGraph


def knightTour(n,path,u,limit):
        print("Current Vertex:{}".format(u))
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = list(u.getConnections())
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    done = knightTour(n+1, path, nbrList[i], limit)
                i = i + 1
            if not done:  # prepare to backtrack
                bt_vertex = path.pop()
                u.setColor('white')
                print("Backtracking vertex {}".format(bt_vertex))
        else:
            done = True
            print("Final path")
            for vertex in path:
                print(vertex)

        return done


path = []
kG = knightGraph(5)
knight_start_position = 15
v=kG.getVertex(knight_start_position)
number_of_squares_to_visit = 18
knightTour(0, path, v, number_of_squares_to_visit)
