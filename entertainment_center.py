"""
Create webpage and open webpage to display movie info and trailers.
"""
import csv
import media
import fresh_tomatoes

HEADER = ["title", "storyline", "poster_image", "trailer_youtube"]
FILENAME = "movies.csv"


def read_movies_from_csv(filename, header):
    """ Read movie info from CSV file into a list of movie objects. """
    try:
        with open(filename, "r") as csvfile:
            movies = []
            reader = csv.DictReader(csvfile, header)
            for row in reader:
                movie = media.Movie(row["title"],
                                    row["storyline"],
                                    row["poster_image"],
                                    row["trailer_youtube"])
                movies.append(movie)
    except FileNotFoundError:
        print("No such file or directory \"{}\".".format(filename))
        exit()
    else:
        if not csvfile.closed:
            csvfile.close()
    return movies


movies = read_movies_from_csv(FILENAME, HEADER)
fresh_tomatoes.open_movies_page(movies)
