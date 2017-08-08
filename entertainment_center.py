import media
import fresh_tomatoes  # This is the module that generates the html file.


la_educacion_prohibida = media.Movie("La Educacion Prohibida",
                        "It describes a variety of alternative education\
                        practices and unconventional schools in \
                        Latin America and Spain.",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/La_Educaci%C3%B3n_Prohibida_%28poster%29.jpg/220px-La_Educaci%C3%B3n_Prohibida_%28poster%29.jpg",  # noqa
                        "https://www.youtube.com/watch?v=BPME2GHBe9s")

rick_and_morty = media.Movie("Rick and Morty",
                 "An animated series that follows the exploits of a\
                 super scientist and his not so bright grandson.",
                 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQxNDEwNTE0Nl5BMl5BanBnXkFtZTgwMzQ1MTg3MDE@._V1_UY268_CR2,0,182,268_AL_.jpg",  # noqa
                 "https://www.youtube.com/watch?v=WNhH00OIPP0")

i_origins = media.Movie("I Origins",
            "A molecular biologist and his laboratory \
            partner uncover evidence that may fundamentally\
            change society as we know it.",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ0MTAwMDI1OF5BMl5BanBnXkFtZTgwNjUwMTA2MTE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
            "https://www.youtube.com/watch?v=Mk4briOLrTQ")

movies = [la_educacion_prohibida, rick_and_morty, i_origins]

fresh_tomatoes.open_movies_page(movies)
