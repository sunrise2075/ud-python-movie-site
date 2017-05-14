import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
						"https://www.youtube.com/watch?v=OqIvPGT3oDQ")

print toy_story.storyline

avatar = media.Movie("Avatar","A marine on an alien planet",
					 "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

print avatar.storyline
# avatar.show_trailer()

transformer = media.Movie("Transformer",
	                 "Transformers is a 2007 American science fiction action film based on the toy line of the same name created by Hasbro",
					 "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",
					 "https://www.youtube.com/watch?v=sgnO5fO46pE")

# print transformer.show_trailer()

movie_list = [toy_story, avatar, transformer]

fresh_tomatoes.open_movies_page(movie_list)