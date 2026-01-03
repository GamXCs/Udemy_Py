raw_ratings = [
    {"title": "  interstellar ", "genre": "sci-fi", "rating": "9"},
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8},
    {"title": "The Dark Knight", "genre": "Action", "rating": "10"},
    {"title": "Parasite", "genre": "thriller", "rating": "9"},
    {"title": "Spirited Away", "rating": "10"},
    {"title": "Mad Max: Fury Road", "genre": "action", "rating": 8},
]


class MovieRating:
    def __init__(self, title, genre, rating):
        self.title = str(title).strip().title()
        self.genre = str(genre).strip().title() if genre else "Other"
        self.rating = int(rating)


class RatingsReport:
    def __init__(self, raw_ratings):
        self.movies = []

        for movie in raw_ratings:
            movie_info = MovieRating(
                title=movie.get("title", ""),
                genre=movie.get("genre"),
                rating=movie.get("rating", 0),
            )
            self.movies.append(movie_info)

    def total_movies(self):
        return len(self.movies)

    def average_rating(self):
        return sum(movie.rating for movie in self.movies) / self.total_movies()

    def group_by_genre(self):
        groups = {}

        for m in self.movies:
            label = m.genre

            if label not in groups:
                groups[label] = []
            groups[label].append(m)
        return groups

    def summary_by_genre(self):
        groups = self.group_by_genre()

        for genre, movies in groups.items():
            count = len(movies)
            avg_rating = sum(m.rating for m in movies) / count
            print(f"{genre}: Count-{count}, Avg Rating:{avg_rating}")
