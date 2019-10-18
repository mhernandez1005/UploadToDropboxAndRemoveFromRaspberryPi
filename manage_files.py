import glob, os
from subprocess import call
import urllib2

def internet_on():
	try:
		urllib2.urlopen('https://www.dropbox.com', timeout=1)
		return True
	except urllib2.URLError as err:
		return False

print "checking for new files"
os.chdir("/home/daq/FTP")
file_list = []

for file in glob.glob("*.jpg"):
	file_list.append(file)

print "done checking for jpg"

if file_list == []:
	print "0 jpg files found"
else:
	print file_list[0]
	print str(len(file_list)) + " jpg files found"

#do a check for internet connection
if internet_on() is True:
	print 'internet connected...'
	if len(file_list) > 0:
		print "new files found...going to upload then remove files"
	        #call(["./dropbox_uploader.sh"," upload","*.jpg"," /"],shell=True)
        	#os.system("./dropbox_uploader.sh upload *.jpg /")
		#call(["sudo","rm","*.jpg"],shell=True)
		#os.system("sudo rm *.jpg")
		for i in range(len(file_list)):
			temp_file = file_list[i]
			upload_str = "./dropbox_uploader.sh upload " + temp_file + " /"
			os.system(upload_str)
			delete_str = "rm -f " + temp_file
			os.system(delete_str)
	else:
		print "no new files found..the program will run again based on cron tab"
elif internet_on() is False:
	print 'no internet connection...'


