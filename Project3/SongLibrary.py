class Song:

    def __init__(self, songRecord):
        tokens = songRecord.split(',')
        if len(tokens) < 7:
            print("incorrect song record")
        else:
            self.title = tokens[1]
            self.artist = tokens[2]
            self.duration = tokens[3]
            self.trackID = tokens[4]
            self.coArtists = tokens[5].split(';')
            self.DNA = tokens[6]

    def toString(self):
        return "Title: " + self.title + ";  Artist: " + self.artist


class SongLibrary:

    def __init__(self):
        self.songArray = list()
        self.isSorted = False
        self.size = 0

    def loadLibrary(self, inputFilename = "TenKsongs_proj3.csv"):

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
    songLib.loadLibrary("TenKsongs_proj3.csv")
    print(songLib.libraryInfo())
