

#get downloaded and unwatched shows from Plex
from PlexRecentUnwatched import readytowatch
try:
	new_plex_eps = readytowatch()
except: Exception, exc:
	new_plex_eps = 'Plex not configured. Adjust settings in config.ini and try again.'

#get upcoming shows from Sonarr
from sonarrComingUp import *
try:
	UpcomingShows = getUpcomingShows() 
except Exception, exc:
	UpcomingShows = 'Sonarr not configured. Adjust settings in config.ini and try again.'

#send the email!
from sendEmailHTML import *

sendanemail(config["Email"]["email_to"],
	'New This Week on Plex',"Here's what's new and ready to watch on Plex: " + 
	'<br> <table cellpadding="5">' + new_plex_eps + 
	"</table><br> New episodes coming this week:" + 
	'<br> <table cellpadding="5">' + UpcomingShows + "</table>")
