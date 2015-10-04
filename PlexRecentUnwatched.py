import plexapi
import datetime
from configobj import ConfigObj
config = ConfigObj('config.ini')
#import variables from config.ini
plex_address = 'http://' + config["Plex"]["plex_address"] + ':' + config["Plex"]["plex_port"]

#establish connection to server
#direct connect
from plexapi.server import PlexServer
plex = PlexServer(plex_address)

#lookup each item in the database. see if it's a week old, if so get metadata and return it
def ep_lookup(epKey):
	item = plex.library.getByKey(epKey)
	week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
	#ep_info = 0
	ep_info_HTML = 0
	if item.addedAt > week_ago:
		#ep_info = item.grandparentTitle + ', "' + item.title + '" Added ' + item.addedAt.strftime("%m-%d-%Y")
		ep_info_HTML = "<tr>\n<td>"+item.grandparentTitle+"</td><td>"+item.title+"</td><td>"+ item.originallyAvailableAt.strftime("%A, %m-%d-%Y") +" </td></tr>"
	return ep_info_HTML
	

def readytowatch():
	new_ep_summary = ''
	header = "<tr><th>Show</th><th>Episode Title</th><th>Air Date</th></tr>"
	for section in plex.library.recentlyAdded():
		if section.librarySectionTitle == 'TV Shows':
			for video in section.unwatched():
				episode = video.ratingKey
				new_shows = ep_lookup(episode)
				if new_shows != 0:
					new_ep_summary += new_shows + "\n"
	new_ep_summary = header + new_ep_summary
	return new_ep_summary



