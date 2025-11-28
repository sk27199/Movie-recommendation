import random

def get_mood():
    mood = input("Enter a mood from this list (happy, sad, bored, hysteria) and I will give you a movie suggestion: ").lower()
    return mood

def get_movie(mood):
    movies = {
        "HAPPY": ["Superman","Avengers","Harry Potter","Wild Robot"],
        "SAD": ["Coco","The Revenant","Interstellar","Whiplash","Her"],
        "BORED": ["Enemy","Prisoners","Nightcrawler","Deadpool","Baby Driver"],
        "HYSTERIA": ["Nice Guys","Palm Springs","Free Guy","Adaptation","Rush Hour"]
    }
    return random.choice(movies.get(mood, ["Being John Malkovich","Seven","Forrest Gump","Fight Club","Die Hard","Taxi Driver"]))

def result(movie):
    print(f"Your movie recommendations: {movie}")


mood = get_mood()
movie = get_movie(mood)
result(movie)