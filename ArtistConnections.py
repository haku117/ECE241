from SongLibrary import SongLibrary, Song

class Vertex:

    def __init__(self, name):
        self.id = name
        self.songs = []
        self.coArtists = {}
        self.edgeList = []
        self.isAcceptingState = None
        self.distance = 99999999 # approximate infinity

    def setAcceptingState(self):
        self.isAcceptingState = True

    def set_distance(self, dist):
        self.distance = dist

    def addEdge(self, e):
        self.edgeList.append(e)

    def add_neighbor(self, nbr):
        if nbr in self.coArtists:
            self.coArtists[nbr] += 1
            return 0
        elif nbr.id != self.id:
            self.coArtists[nbr] = 1
            return 1
        return 0

    def followEdge(self, c):
        for i in self.edgeList:
            if i.character == c:
                return i.destination
        return None


class Edge:
    def __init__(self, c, dest):
        self.destination = dest
        self.character = c


class ArtistConnections:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.numEdges = 0
        self.edgeList = []

    """
    Load the artist connections graph based on a given song database
    Add the edges based on the last column of the collaborative artists 

    """
    def load_graph(self, file_name="TenKsongs_proj3.csv", limit=500):
        
        song_lib = SongLibrary()

        file = open(file_name, 'r')
        line_array = file.readlines()

        count = 0
        for line in line_array:
            song_obj = Song(line)
            song_lib.songArray.append(song_obj)
            self.insert_vert(song_obj)
            count += 1
            if count > limit:
                break

        file.close()
        return self.numVertices

    """
    Parse the song object, generate vertices, insert them to the graph 
    """
    def insert_vert(self, song_obj):

        # create or retrieve artist vertex
        if song_obj.artist in self.vertList:
            vert = self.vertList[song_obj.artist]
        else:
            vert = Vertex(song_obj.artist)
            self.vertList[song_obj.artist] = vert
            self.numVertices += 1

        # add vertex information
        vert.songs.append(song_obj.title)

        # add edges from coArtists
        for nbr in song_obj.coArtists:
            # create or retrieve neighbor vertex
            if nbr in self.vertList:
                nbr_vert = self.vertList[nbr]
            else:
                nbr_vert = Vertex(nbr)
                self.vertList[nbr] = nbr_vert
                self.numVertices += 1

            # add edges
            self.numEdges += vert.add_neighbor(nbr_vert)
            nbr_vert.add_neighbor(vert)

    """
    Return song library information
    """
    def graph_info(self):
        return "Vertex Size: " + str(self.numVertices) + "\t total Edges: " + str(self.numEdges)

    """
    Compute the shortest path distance from source vertex s to each vertex in the vertList 
    """
    def BellmanFord(self, s):

        if s not in self.vertList:
            print("Wrong artist name ", s)
            return

        s_vert = self.vertList[s]
        s_vert.set_distance(0)

        #
        # Write your code here
        #

        return


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':

    artistGraph = ArtistConnections()
    artistGraph.load_graph()
    print(artistGraph.graph_info())

    artistGraph.BellmanFord("Mariah Carey")
