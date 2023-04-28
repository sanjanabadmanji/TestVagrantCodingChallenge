class Store_Song:
    def __init__(self, capacity):
        self.data = {}
        self.capacity = capacity
        
    
    def song(self, user, song):
        if user not in self.data:
            self.data[user] = []
        if song in self.data[user]:
            self.data[user].remove(song)
        elif len(self.data[user]) == self.capacity:
            self.data[user].pop(0)
        self.data[user].append(song)
    
    def Recently_Played_Song(self, user):
        if user not in self.data:
            return []
        return self.data[user]

store = Store_Song(3)
store.song("user_1", "S1")
store.song("user_1", "S2")
store.song("user_1", "S3")

print(store.Recently_Played_Song("user_1"))
store.song("user_1", "S4")

print(store.Recently_Played_Song("user_1"))
store.song("user_1", "S2")

print(store.Recently_Played_Song("user_1"))
store.song("user_1", "S1")

print(store.Recently_Played_Song("user_1"))