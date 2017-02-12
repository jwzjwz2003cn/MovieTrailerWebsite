import webbrowser

class Movie():
	""" A movie class describes a movie object
	Args:
		title (str): title of the movie
		storyline (str): the plot of the movie
		poster_image_url(str): movie's poster image url
		trailer_youtube(str): movie's youtube trailer url

	__init__
		Args:
			movie_title(str),
			movie_storyline(str),
			poster_image(str),
			trailer_youtube(str)

	"""
	def __init__(self, movie_title, movie_storyline, poster_image, 
				trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		# show movie's trailer on youtube
		webbrowser.open(self.trailer_youtube_url)