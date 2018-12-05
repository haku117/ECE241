
class Song:

    def __init__(self, songRecord):
        tokens = songRecord.split(',')
        if len(tokens) != 5:
            print("incorrect song record")
        else:
            self.title = tokens[1]
            self.artist = tokens[2]
            self.duration = tokens[3]
            self.trackID = tokens[4]

    def toString(self):
        return "Title: " + self.title + ";  Artist: " + self.artist


class SongLibrary:

    def __init__(self):
        self.songArray = list()
        self.isSorted = False
        self.size = 0

    def loadLibrary(self, inputFilename):

        with open(inputFilename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                song = Song(line)
                self.songArray.append(song)
                self.size += 1

        file.close()

    """
    Return song libary information
    """
    def libraryInfo(self):
        return "Size: " + str(self.size) + ";  isSorted: " + str(self.isSorted)


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    songLib = SongLibrary()
    songLib.loadLibrary("TenKsongs_proj2.csv")
    print(songLib.libraryInfo())

