class Store_Song:
    def __init__(self, capacity):
        self.data = {}
        self.capacity = capacity
        
    
    def add_song(self, user, song):
        if user not in self.data:
            self.data[user] = []
        if song in self.data[user]:
            self.data[user].remove(song)
        elif len(self.data[user]) == self.capacity:
            self.data[user].pop(0)
        self.data[user].append(song)
    
    def RecentlyPlayedSong(self, user):
        if user not in self.data:
            return []
        return self.data[user]

store = Store_Song(3)
store.add_song("user1", "S1")
store.add_song("user1", "S2")
store.add_song("user1", "S3")
print(store.RecentlyPlayedSong("user1"))
store.add_song("user1", "S4")
print(store.RecentlyPlayedSong("user1"))
store.add_song("user1", "S2")
print(store.RecentlyPlayedSong("user1"))
store.add_song("user1", "S1")
print(store.RecentlyPlayedSong("user1"))