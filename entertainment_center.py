"""
Create  webpage info & trailers of  some of my favourite movies.
"""

import media
import fresh_tomatoes

riddick = media.Movie("Riddick",
                      "Escaped criminal, Riddick is left for dead on a "
                      "deserted planet.",
                      "https://upload.wikimedia.org/wikipedia/en/6/69/Riddick_poster.jpg",
                      "https://www.youtube.com/watch?v=iP3eFIOBU0k")

hardcore_henry = media.Movie("Hardcore Henry",
                             "Henry is revived from an accident with no "
                             "memory and must save his wife from meceneries.",
                             "https://upload.wikimedia.org/wikipedia/en/e/ed/Hardcore_%282015_film%29.jpg",
                             "https://www.youtube.com/watch?v=96EChBYVFhU")

deadpool = media.Movie("Deadpool",
                       "Wade Wilson, a former Special Forces operative is "
                       "subjected to a rogue experiment that gives him "
                       "accelerated healing powers and a horribly disfgured "
                       "face.",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=9vN6DHB6bJc")

the_man_from_uncle = media.Movie("The Man From Uncle",
                                 "A professional thief-turned CIA agent "
                                 "Napoleon Solo must work on a joint mission "
                                 "with a operative Illya Kuryakin.",
                                 "https://upload.wikimedia.org/wikipedia/en/e/e5/The_Man_from_U.N.C.L.E._poster.jpg",
                                 "https://www.youtube.com/watch?v=CzYRlISYE8Y")

furious_7 = media.Movie("Furious 7",
                        "Dominic Toretto must hunt down Deckard Shaw.",
                        "https://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg",
                        "https://www.youtube.com/watch?v=yISKeT6sDOg")

hateful_eight = media.Movie("Hateful Eight",
                            "A bounty hunter is transporting three dead "
                            "bounties",
                            "https://upload.wikimedia.org/wikipedia/en/d/d4/The_Hateful_Eight.jpg",
                            "https://www.youtube.com/watch?v=gnRbXn4-Yis")

movies = [riddick, hardcore_henry, deadpool, the_man_from_uncle, furious_7,
          hateful_eight]
fresh_tomatoes.open_movies_page(movies)
