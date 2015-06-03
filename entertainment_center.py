import media
import fresh_tomatoes

# instatiate th movie objects
hunger_games = media.Movie("Hunger Games",
                        "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised fight to the death in which two teenagers from each of the twelve Districts of Panem are chosen at random to compete.",
                        "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=PbA63a7H0bo",
                        "23 March 2012 (USA)")

midnight_in_paris = media.Movie("Midnight in Paris",
                        "While on a trip to Paris with his fiancee's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s every day at midnight.",
                        "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://youtu.be/BYRWfS2s2v4",
                        "10 June 2011 (USA)")

school_of_rock = media.Movie("School of Rock",
                        "When struggling musician Dewey Finn finds himself out of work, he takes over his roommate's job as an elementary school substitute teacher and turns class into a rock band.",
                        "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=3PsUJFEBC74",
                        "3 October 2003 (USA)")

avatar = media.Movie("Avatar",
                        "A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home..",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://youtu.be/5PSNL1qE6VY",
                        "18 December 2009 (USA)")

ratatouille = media.Movie("Ratatouille",
                        "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                        "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                        "29 June 2007 (USA)")

toy_story= media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        "22 November 1995 (USA)")


# create the list of movies
movies = [hunger_games, midnight_in_paris, school_of_rock, avatar, ratatouille, toy_story]


# launch the web page displaying the movies 
fresh_tomatoes.open_movies_page(movies)


