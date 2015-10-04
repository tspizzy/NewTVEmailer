import requests
import pprint
import datetime
from configobj import ConfigObj
config = ConfigObj('config.ini')


def getUpcomingShows():
	endpoint = "http://" + config["Sonarr"]["sonarr_address"] + ":" + config["Sonarr"]["sonarr_port"] + "/api/Calendar"
	show_list = ''
	show_list_HTML = "<tr><th>Show</th><th>Episode Title</th><th>Air Date</th></tr>"
	apikey = config["Sonarr"]["sonarr_apikey"]

	start_date = datetime.datetime.now()
	end_date = datetime.datetime.now() + datetime.timedelta(days=7)

	query_params = { 'apikey': apikey,
		'start' : start_date,
		'end' : end_date
	}


	response = requests.get(endpoint, params = query_params)
	#print response.url

	data = response.json()
	for show in data:
		show_title = show['series']['title']
		episode_title = show['title']
		airDate = show['airDate']
		airDate = datetime.datetime.strptime(airDate, '%Y-%m-%d')
		#print show_title.encode("utf8") + ' ' + episode_title.encode("utf8") +' ' + airDate.strftime('%A, %m %d') 
		#show_list = show_list + show_title + ' ' + episode_title +' ' + airDate.strftime('%A, %m %d') + '\n'
		show_list_HTML = show_list_HTML + "<tr>\n<td>"+show_title.encode("utf8")+"</td><td>"+episode_title.encode("utf8")+"</td><td>"+ airDate.strftime("%A, %m-%d-%Y") +" </td></tr>"
	return show_list_HTML

