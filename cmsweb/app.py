# This script uses the flask webserver to display the stats gathered by the CMSStatus.py
# This script does not force a refresh of the browser but does refresh the information in the html template
# you can install the auto refresh plugin to force the browser to update at a frequency that you choose
#Import the flask webserver libray
from flask import Flask, render_template

# This section imports the variables created by the CMSStatus.py these will be used as variables for HTML
from stats import host_id
from stats import software_version
from stats import uptime_seconds
from stats import call_legs_active



# Webserver config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
	
# The  html template here uses the previously imported variables and sets the weblink for the CMSStats Page
# the html templates are contained in the folder structure.

@app.route('/CMSStats')
def CMSStats():
	return render_template('CMS-Live-Stats.html', host_id = host_id, software_version = software_version, uptime_seconds = uptime_seconds, call_legs_active = call_legs_active)
	

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
	
