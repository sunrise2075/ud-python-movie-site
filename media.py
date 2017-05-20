import webbrowser

class Movie():

	"""
		This class provides a way to store movie related information
	"""
	valid_ratings = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
		"""
			constructor of the python object which is currently under construction
			@param self  the python object which is currently under construction
			@param movie_title
			@param movie_storyline
			@param poster_image_url
			@param trailer_youtube_url
		"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url


	def show_trailer(self):
		"""
			open a browser window which is navigated to a youtub page of the movie trailer
		"""
		webbrowser.open(self.trailer_youtube_url)