# CMS API status call to web page
Repository for my CMS API call scripts

There are a number of scripts here to allow an API call to log into Cisco meeting server and poll the API for status.

The API status is returned as an XML output

The XML is written to file.

The file is read back in and parsed using element tree to create variables for the CMSStats html template page in flask

CMSStatus.py does the API call

app.py runs the flask web server and the CMSStats template variables are updated every time the CMSStatus.py uses the scheduler which is currently every minute.

Set the file up in a folder running C:\CMSStats or change the file paths in the script to match you directories for these file.

Ther is nothing in the flask server script to force the client end to refresh the page so you need to add the ajax or javascript to do this. Alternatively add the google automatic refresh plugin.

This is a demo to show how these API stats could be utilised on a webserver.





