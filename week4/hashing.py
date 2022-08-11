class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return f"{self.key}"
 
class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.count = 0
    def getSlots(self):
        return str([str(slot) for slot in self.slots])
    def getData(self):
        return str([str(data) for data in self.data])
    def hashfunction(self,key):
        h = 0
        for char in str(key):
            h += ord(char)
        return h % self.size
    def rehash(self,key):
        # Insert your secondary hashing function code
        keystr = str(key)
        hashVal = 0
        counter = 0
        for ch in str(keystr):
            counter += 1
            hashVal += ord(ch)+counter
        return (hashVal*len(keystr)) % self.size
    def put(self,key,data):
        # Insert your code here to store key and data
        item = HashItem(key, data)
        h = self.hashfunction(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h + 1) % self.size
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item
    def get(self,key):
        # Insert your code here to get data by key
        h = self.hashfunction(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h + 1) % self.size
        return None
    def __getitem__ (self,key):
        return self.get(key)
    def __setitem__ (self,key,data):
        self.put(key,data)
    def __repr__(self):
        return str([str(slot) for slot in self.slots])

H = HashTable()
H[69] = 'A'
H[66] = 'B' 
H[80] = 'C' 
H[35] = 'D' 
H[18] = 'E' 
H[52] = 'F' 
H[89] = 'G' 
H[70] = 'H' 
H[12] = 'I' 

print(H.getSlots())

print(H.get(52))