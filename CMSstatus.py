#This script does an API call on the Cisco Meeting server stats
#The script polls CMS and writes the stats to the webserver folder every minute in .xml

#This imports the requests library
import requests
#This imports the schedule and time modules so that the functions can be run at a regular interval
import schedule
import time

#imports Prettyprint to present responses in readable format if required
import pprint

# Allows the OS library to be imported to allow the folders to be changed
import os

# Imports ElementTree for parsing XML data
import xml.etree.ElementTree as ET

#imports auth credentials store in file basicauth.py
from basicauth import basic



#URL to be used in API Call. Set the IP address of the CMS Server here or import and referece the variable
url = "https://<cms-ip-address>:445/api/v1/system/status"



payload = {}

# Sets the auth header to use the imported basic variable
headers = {
  'Authorization': (basic),
  'Cookie': 'session=logout'
  

}

# This function polls CMS and requests the status which it saves in xml format in the defined working directory
def CMSstats():
	os.chdir("C:\CMSstats")
	response = requests.request("GET", url, headers=headers, data = payload, verify=False)
	pprint.pprint(response)
	print(response.text.encode('utf8'))
	with open('CMSstats.xml', 'w') as f:
		f.write(response.text)
		

# This function parses the XML data into a variables which are saved and called by the html code of the web server
# The folder is changed to the webserver route and the file is saved there
def CMSStatsformat():
	tree = ET.parse("CMSStats.xml")
	root = tree.getroot()

	host_id = (root[0]).text
	software_version = (root[1]).text
	uptime_seconds = (root[2]).text
	call_legs_active = (root[7]).text
	call_legs_maxactive = (root[8]).text
	call_legs_completed = (root[9]).text
	audio_bit_rateincoming = (root[10]).text
	audio_bit_rateoutgoing = (root[11]).text
	video_bit_rateincoming = (root[12]).text
	video_bit_rateoutgoing = (root[13]).text

	os.chdir("C:\CMSStats\cmsweb")

	with open("stats.py","w") as f:
		print("host_id = '"+(host_id)+"'"+"\n"+"software_version = "+(software_version)+"\n"+"uptime_seconds = "+(uptime_seconds)+"\n"+"call_legs_active = "+(call_legs_active)+"\n"+"call_legs_maxactive = "+(call_legs_maxactive)+"\n"+"call_legs_completed = "+(call_legs_completed)+"\n"+"audio_bit_rateincoming = "+(audio_bit_rateincoming)+"\n"+"audio_bit_rateoutgoing = "+(audio_bit_rateoutgoing)+"\n"+"video_bit_rateincoming = "+(video_bit_rateincoming)+"\n"+"video_bit_rateoutgoing = "+(video_bit_rateoutgoing), file=f)



# the shedule sets both the tasks to run every minute	
schedule.every(1).minutes.do(CMSstats)

schedule.every(1).minutes.do(CMSStatsformat)

while True:
    schedule.run_pending()
    time.sleep(1)


