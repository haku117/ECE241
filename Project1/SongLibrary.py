"""
UMass ECE 241 - Advanced Programming
Project #1     Fall 2018
SongLibrary.py - SongLibrary class
"""

from Song import Song
import random
import time

class SongLibrary:

    """
    Intialize your Song library here. 
    You can initialize an empty songArray, empty BST and 
    other attributes such as size and whether the array is sorted or not
    
    """
    def __init__(self):
        self.songArray = list()
        self.songBST = None
        self.isSorted = False
        self.size = 0


    """
    load your Song library from a given file. 
    It takes an inputFilename and store the songs in songArray
    """
    def loadLibrary(self, inputFilename):
        #
        # Write your code here
        #

    """
    Linear search function. 
    It takes a query string and attibute name (can be 'title' or 'artist')
    and return the number of songs fonud in the library.
    Return -1 if no songs is found.
    Note that, Each song name is unique in the database, 
    but each artist can have several songs.
    """
    def linearSearch(self, query, attribute):
        found = -1
        #
        # Write your code here
        #

        return found

    """
    Build a BST from your Song library based on the song title. 
    Store the BST in songBST variable
    """
    def buildBST(self):
        #
        # Write your code here
        #

    """
    Implement a search function for a query song (title) in the songBST.
    Return the song information string
    (After you find the song object, call the toString function)
    or None if no such song is found.
    """
    def searchBST(self, query):
        #
        # Write your code here
        #

    """
    Return song libary information
    """
    def libraryInfo(self):
        return "Size: " + str(self.size) + ";  isSorted: " + str(self.isSorted)


    """
    Sort the songArray using QuickSort algorithm based on the song title.
    The sorted array should be stored in the same songArray.
    Remember to change the isSorted variable after sorted
    """
    def quickSort(self):
        #
        # Write your code here
        #


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    
    songLib = SongLibrary()
    songLib.loadLibrary("TenKsongs.csv")
    print(songLib.libraryInfo())