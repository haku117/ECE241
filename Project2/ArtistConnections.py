import random


class ArtistConnections:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    """
    Load the artist connections graph based on a given song database
    Add the edges based on the last column of the collaborative artists 
    
    """
    def load_graph(self, songLibaray):

        #
        # Write your code here
        #
        return self.numVertices

    """
    Return song libary information
    """
    def graph_info(self):
        return "Vertex Size: " + str(self.numVertices)

    """
    Search the information of an artist based on the artist name
    Return a tuple (the number of songs he/she wrote, the collaborative artist list)

    """
    def search_artist(self, artist_name):

        numSongs = 0;
        artistLst = []

        #
        # Write your code here
        #

        return numSongs, artistLst

    """
    Return a list of two-hop neighbors of a given artist
    """
    def find_new_friends(self):

        two_hop_friends = []

        #
        # Write your code here
        #
        return two_hop_friends

    """
    Search the information of an artist based on the artist name

    """
    def recommend_new_collaborator(self, artist_name):

        artist = ""
        numSongs = 0

        #
        # Write your code here
        #

        return artist, numSongs

    """
    Search the information of an artist based on the artist name

    """
    def shortest_path(self, artist_name):

        path = {}

        #
        # Write your code here
        #
        return path


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    artistGraph = ArtistConnections()

    ArtistConnections.generate_data("TenKsongs_proj2.csv")
