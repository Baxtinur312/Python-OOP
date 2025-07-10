class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration  
        self.rating = rating  

movie1 = Movie("Inception", "Sci-Fi", 148, 8.8)
print("Title:", movie1.title)
print("Genre:", movie1.genre)
print("Duration:", movie1.duration, "minutes")
print("Rating:", movie1.rating)