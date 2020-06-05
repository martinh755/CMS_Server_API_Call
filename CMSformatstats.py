import os
import xml.etree.ElementTree as ET
os.chdir("C:\CMSStats")

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



	

