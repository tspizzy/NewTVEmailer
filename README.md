# NewTVEmailer
Collects latest unwatched additions to Plex and next week's coming shows from Sonarr then emails them to a designated address.
The script will collect a list unwatched tv episodes that were added to Plex in the last 7 days and return the show title, episode title, and air date. From Sonarr, the script will collect a list of episodes that will air in the next 7 days and display the same metadata. This data is emailed to the designated address.


##Configuration
Fill in the config.ini file by entering the settings to connect to your Plex, Sonarr, and email. Make sure that each of your settings is enclosed in a single quote. 

##Automation
For best results, try setting up an automated task to run the NewTVEmailer.py script each week. 

###Known bugs
Movies that have been added to Plex are not showing up in the list of added content.
