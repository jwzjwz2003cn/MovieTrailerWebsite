import media
import fresh_tomatoes

# define a list of movie objects
sw_ep1 = media.Movie("Star Wars Episode I: The Phantom Menance", 
	"Jar Jar binks' space adventure and pod race",
	"https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_"
	"Menace_poster.jpg",
	"https://www.youtube.com/watch?v=bD7bpG-zDJQ")

sw_ep2 = media.Movie("Star Wars Episode II: Attack of the Clones",
	"Yoda kicked some serious ass",
	"https://upload.wikimedia.org/wikipedia/en/3/32/Star_Wars_-_Episode_II"
	"_Attack_of_the_Clones_%28movie_poster%29.jpg",
	"https://www.youtube.com/watch?v=gYbW1F_c9eM")

sw_ep3 = media.Movie("Star Wars Episode III: Revenge of the Sith",
	"It's over Anakin, I have the high ground",
	"https://upload.wikimedia.org/wikipedia/en/9/93/Star_Wars_Episode_III"
	"_Revenge_of_the_Sith_poster.jpg",
	"https://www.youtube.com/watch?v=5UnjrG_N8hU")

sw_ep4 = media.Movie("Star Wars Episode IV: A New Hope",
	"Death Star blows up due to some serious design flaws",
	"https://upload.wikimedia.org/wikipedia/en/8/87/"
	"StarWarsMoviePoster1977.jpg",
	"https://www.youtube.com/watch?v=1g3_CFmnU7k")

sw_ep5 = media.Movie("Star Wars Episode IV: Empire Strikes Back",
	"A story about the father and the son reunion", 
	"https://upload.wikimedia.org/wikipedia/en/3/3c/"
	"SW_-_Empire_Strikes_Back.jpg",
	"https://www.youtube.com/watch?v=JNwNXF9Y6kY")

sw_ep6 = media.Movie("Star Wars Episode VI: Return of the Jedi", 
	"Best fan service in history with Leia in Golden Bikini",
	"https://upload.wikimedia.org/wikipedia/en/b/b2/"
	"ReturnOfTheJediPoster1983.jpg",
	"https://www.youtube.com/watch?v=7L8p7_SLzvU")

sw_ep7 = media.Movie("Star Wars Episode VII: The Force Awakens", 
	"Bad ass trained dark force user got beat up by a newbie",
	"https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens"
	"_Theatrical_Poster.jpg",
	"https://www.youtube.com/watch?v=sGbxmsDFVnE")

movies = [sw_ep1, sw_ep2, sw_ep3,sw_ep4, sw_ep5, 
		  sw_ep6, sw_ep7]

# dynamically generating the movies page using fresh_tomatoes API		  
fresh_tomatoes.open_movies_page(movies)
