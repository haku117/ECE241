from ArtistConnections import Vertex, Edge
from SongLibrary import SongLibrary

class DFA:

    def __init__(self, s=None):
        self.start = s

    """
    Build the DFA graph from the figure in task 2

    """
    def build_DFA(self):

        #
        # Write your code here
        #

        return

    """
    Test whether the input sequence seq will be accepted by the state machine
    return True if accept

    """
    def testMatch(self, seq):

        #
        # Write your code here
        #

        return False

    """
    Test whether the one suffix of the input sequence seq will be accepted by the state machine
    return the index position if accept
    return -1 if not accept

    """
    def testAccept(self, seq):

        indx = -1

        #
        # Write your code here
        #

        return indx

    """
    For every song in the song library array, test whether they will be accepted by the state machine
    Store the match index or -1 into the matchIndx array.
    Please make sure the order of songs in the songlibrary is the same as the input file

    """
    def testSongLibrary(self, song_lib):

        matchIndx = []

        #
        # Write your code here
        #

        return matchIndx


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':

    dfa = DFA()
    dfa.build_DFA()
    song_lib = SongLibrary()
    song_lib.loadLibrary()
    dfa.testSongLibrary(SongLibrary)

    print("finish")