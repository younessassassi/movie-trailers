import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                        "Avatar description",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://www.youtube.com/watch?v=vwyZH85NQC4")


# create the list of movies
movies = [toy_story, avatar]


# launch the movies 
fresh_tomatoes.open_movies_page(movies)


#avatar.show_trailer()
