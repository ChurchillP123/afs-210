from tokenize import maybe
import random

class Song:
    def __init__(self,title=None,artist=None):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None
    def getTitle(self):
        return self.title
    def getArtist(self):
        return self.artist
    def setNext(self, song):
        self.next = song
    def __str__(self):
        return self.title + " by " + self.artist 
    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)
    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.curr = None
        self.count = 0
    def getCount(self):
        return self.count
    def addSong(self, song) -> None:
        if self.head is None:
            self.head = self.tail = song
        else:
            self.tail.next = song
            song.prev = self.tail
            song.next = None
            self.tail = song
        self.count += 1
    def deleteSong(self, title):
        curr = self.head
        prev = self.head
        while curr:
            if curr.title == title:
                if curr == self.tail:
                    prev.next = None
                    self.tail = prev
                elif curr == self.head:
                    curr.next.prev = None
                    self.head = curr.next
                else:
                    prev.next = curr.next
                    curr.next = prev
                return
            prev = curr
            curr = curr.next
    def getCurrent(self):
        return self.curr
    def play(self):
        self.curr = self.head
        return self.getCurrent()
    def skip(self):
        if (self.curr.next):
            self.curr = self.curr.next
            return self.getCurrent()
        else:
            self.curr = self.head
            return self.getCurrent()
    def prev(self):
        if (self.curr.prev):
            self.curr = self.curr.prev
            return self.getCurrent()
        else:
            self.curr = self.tail
            return self.getCurrent()
    def shuffle(self):
        usedValues = {}
        x = 0
        length = 0
        for song in self.iter():
            length = len(usedValues)
            x = random.randint(0, self.count-1)
            usedValues.add(x)
            while length == len(usedValues):
                x = random.randint(0, self.count-1)
            song.setNext(self[x])
            
    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        curr = self.head
        for n in range(index):
            curr = curr.next
        return curr
    def __setitem__(self, index, song):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        curr = self.head
        for n in range(index):
            curr = curr.next
        curr = song
    def iter(self):
        # Iterate through the list.
        curr = self.head
        while curr:
            val = curr
            curr = curr.next
            yield val
    def __str__(self):
        myStr = ""
        for song in self.iter():
            myStr += str(song)+ " \n"
        return myStr

myPlaylist = Playlist()

while True:
    menu()
    choice = int(input())
    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        title = input('What is the Title of the Song?: ')
        artist = input('What is the Artist Name?: ')
        song = Song(title, artist)
        # Add song to playlist
        myPlaylist.addSong(song)
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title
        title = input('What is the Title of the Song?: ') 
        # remove song from playlist
        myPlaylist.deleteSong(title)
        print("Song Removed to Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....") 
        print(myPlaylist.play())
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")
        print(myPlaylist.skip())             
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")
        print(myPlaylist.prev())  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")
        myPlaylist.shuffle()
        print(myPlaylist)
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing:", end=" ")   
        print(myPlaylist.getCurrent())
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        print(myPlaylist)
    elif choice == 0:
        print("Goodbye.")
        break