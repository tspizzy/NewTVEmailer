import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configobj import ConfigObj
config = ConfigObj('config.ini')

def sendanemail(recipient, subject, message):
	username = config["Email"]["email_user"]
	password = config["Email"]["email_pass"]


	# me == my email address
	# you == recipient's email address
	From = config["Email"]["email_from"]
	To = recipient

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = From
	msg['To'] = To


	# Create the body of the message (a plain-text and an HTML version).
	#text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
	html = message

	
	html_msg = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	
	msg.attach(html_msg)

	server = smtplib.SMTP(config["Email"]["smtp_server"] +':'+config["Email"]["smtp_port"])
	server.starttls()
	server.login(username,password)
	server.sendmail(From, To, msg.as_string())
	server.quit()
