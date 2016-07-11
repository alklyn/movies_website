# Movie website


## What is it
A Movie Trailer Website where users can see my favorite movies and watch the
trailers.


## Project files
File                    | Purpose
----------------------- | ----------------------------------------------------
media.py                | Contain the classes needed to create movie objects.
fresh_tomatoes.py       | Generate the website from a list of movie objects.
movies.csv              | Store movie info.
entertainment_center.py | Create the wesite using the modules and file above.


## Requirements
 Make sure you have Python 2.7 installed on your computer.
 [Python](https://www.python.org)


## How do you use it?
In the command line enter the directory movie_website & type:

`python entertainment_center.py`

This will create the the web page "fresh_tomatoes.html" as well as open it in
your default browser. Click on a movie's poster to play it's trailers.

### How do you change movies displayed?
Simply open the file "movies.csv" in a spreadsheet of your choice.
You'll find the data is split into the following columns

title | storyline | poster_image | trailer_youtube

When you're done editing save the file as CSV with the following settings:

Field delimiter: ,
Text delimiter: "

Then type again:

`python entertainment_center.py`

to create and open the new webpage.
