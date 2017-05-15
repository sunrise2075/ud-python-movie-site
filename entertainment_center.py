import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=OqIvPGT3oDQ")

print toy_story.storyline


avatar = media.Movie("Avatar","A marine on an alien planet",
					 "https://upload.wikimedia.org/wikipedia/zh/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

print avatar.storyline
# avatar.show_trailer()

transformer = media.Movie("Transformer",
	                 "Transformers is a 2007 American science fiction action film based on the toy line of the same name created by Hasbro",
					 "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",
					 "https://www.youtube.com/watch?v=sgnO5fO46pE")

citizenKane = media.Movie("Citizen Kane",
	                 "Citizen Kane is a 1941 American mystery drama film by Orson Welles",
					 "https://upload.wikimedia.org/wikipedia/en/c/ce/Citizenkane.jpg",
					 "https://www.youtube.com/watch?v=8dxh3lwdOFw")

twelveAngryMen = media.Movie("12 Angry men",
	                 "12 Angry Men is a 1957 American courtroom drama film adapted from a teleplay of the same name by Reginald Rose",
					 "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg",
					 "https://www.youtube.com/watch?v=gieIAysQTI0")

toLive = media.Movie("To Live",
	                 "A story about a Chinese family who is living on the yellow oil in China",
					 "https://upload.wikimedia.org/wikipedia/zh/5/5c/%E7%94%B5%E5%BD%B1%E6%B4%BB%E7%9D%80.jpg",
					 "https://www.youtube.com/watch?v=iEe0XwfbIl4")

# print transformer.show_trailer()

movie_list = [
	toy_story, avatar, transformer, citizenKane,
	twelveAngryMen, toLive
]

fresh_tomatoes.open_movies_page(movie_list)

# print media.Movie.__doc__

# print media.Movie.__name__

# print media.Movie.__module__