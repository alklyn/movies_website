import media

riddick = media.Movie("Riddick",
                       "Escaped criminal, Riddick is left for dead on a "
                       "deserted planet.",
                       "https://upload.wikimedia.org/wikipedia/en/6/69/Riddick_poster.jpg",
                       "https://www.youtube.com/watch?v=iP3eFIOBU0k")

hardcore_henry = media.Movie("Hardcore Henry",
                       "Henry is revived from an accident with no memory and "
                       "must save his wife from meceneries.",
                       "https://upload.wikimedia.org/wikipedia/en/e/ed/Hardcore_%282015_film%29.jpg",
                       "https://www.youtube.com/watch?v=96EChBYVFhU")

deadpool = media.Movie("Deadpool",
                       "Wade Wilson, a former Special Forces operative is "
                       "subjected to a rogue experiment that gives him "
                       "accelerated healing powers and a horribly disfgured "
                       "face.",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=9vN6DHB6bJc")

print(deadpool.storyline)
deadpool.show_trailer()
